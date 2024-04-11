from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode: pass


class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body


class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    


class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast, ):
        self.ast = ast
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = [{
                "readNumber" : FuncZcode([], NumberType(), True),
                "readBool" : FuncZcode([], BoolType(), True),
                "readString" : FuncZcode([], StringType(), True),
                "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
                "writeBool" : FuncZcode([BoolType()], VoidType(), True),
                "writeString" : FuncZcode([StringType()], VoidType(), True)
                }]
       
        
    def check(self):
        self.visit(self.ast, [{}])
        return None    
    
    
    def comparType(self, LHS, RHS): 
        if (type(LHS) is ArrayType) and (type(RHS) is ArrayType):
            if type(LHS.eleType) != type(RHS.eleType) or (len(LHS.size) != len(RHS.size)):
                return False
            
            for i in range(0, len(LHS.size)):
                if LHS.size[i] != RHS.size[i]:
                    return False
            
            return True
                
        return type(LHS) == type(RHS)
        
        
    def comparListType(self, LHS, RHS): 
        if len(LHS) != len(RHS):
            return False
        
        for i in range(0, len(LHS)):
            if not self.comparType(LHS[i], RHS[i]):
                return False
            
        return True
    
    
    # decl: List[Decl]  
    def visitProgram(self, ast, param): 
        for decl in ast.decl: 
            self.visit(decl, param)
            
        for key, value in self.listFunction[0].items():
            if not value.body:
                raise NoDefinition(key)
        
        mainFunc = self.listFunction[0].get("main")
        if (mainFunc is None) or (type(mainFunc.typ) != VoidType) or (len(mainFunc.param) > 0):
            raise NoEntryPoint()
 
    
    # class VarDecl(Decl, Stmt): name: Id , varType: Type , modifier: str = None , varInit: Expr = None  
    def visitVarDecl(self, ast, param):
        if param[0].get(ast.name.name):
            raise Redeclared(Variable(), ast.name.name) 
    
        param[0][ast.name.name] = VarZcode(ast.varType)  
      
        if ast.varInit: 
            left = param[0].get(ast.name.name).typ if ast.varType else param[0].get(ast.name.name)
            right = self.visit(ast.varInit, param)
            
            if isinstance(left, Zcode) and isinstance(right, Zcode):
                raise TypeCannotBeInferred(ast)
            
            elif isinstance(left, Zcode):
                left.typ = right
            elif isinstance(right, Zcode):  
                right.typ = left
            elif not self.comparType(left, right):
                raise TypeMismatchInStatement(ast)
        
        return param


    def verifyParamDeclaration(self, ast, param):
        # Check if the name exists in the arguments
        if param[0].get(ast.name.name):
            raise Redeclared(Parameter(), ast.name.name) 
            
        param[0][ast.name.name] = VarZcode(ast.varType)

        
    # class FuncDecl(Decl):  name: Id , param: List[VarDecl] , body: Stmt = None 
    def visitFuncDecl(self, ast, param):
        typeParam = []  
        listParam = [{}]  
        
        for paramDecl in ast.param:
            self.verifyParamDeclaration(paramDecl, listParam)
            typeParam.append(paramDecl.varType)
            
        self.Return = False
        exitFunction = self.listFunction[0].get(ast.name.name)
         
        if exitFunction:
            if exitFunction.body:
                raise Redeclared(Function() , ast.name.name)
            
            elif not ast.body:
                raise Redeclared(Function() , ast.name.name)
            
            elif not self.comparListType(typeParam , exitFunction.param):
                raise Redeclared(Function() , ast.name.name)

            self.listFunction[0][ast.name.name].body = True 
            
        else: 
            self.listFunction[0][ast.name.name] = FuncZcode(typeParam , None , ast.body)
        
        if ast.body: 
            self.function = self.listFunction[0].get(ast.name.name)
            self.visit(ast.body , listParam + param)
            self.function = None

            if not self.Return:
                if self.listFunction[0][ast.name.name].typ is None:
                    self.listFunction[0][ast.name.name].typ = VoidType()
                elif not self.comparType(self.listFunction[0][ast.name.name].typ, VoidType()): 
                    raise TypeMismatchInStatement(Return(None))
        
        return self.listFunction
        
    # class Id(LHS): name: str
    def visitId(self, ast, param):  
        for varDeclList in param:
            var = varDeclList.get(ast.name)
            
            if var and var.typ:
                return var.typ 
            
            elif var and not var.typ:
                return var
                
        raise Undeclared(Identifier() , ast.name)


    # class CallStmt(Stmt): name: Id {name : str} , args: List[Expr] 
    def visitCallStmt(self, ast, param):
        func = self.listFunction[0].get(ast.name.name)
        
        if not func: 
            raise Undeclared(Function() , ast.name.name)
        
        if len(ast.args) != len(func.param):
            raise TypeMismatchInStatement(ast)
        
        for i in range(len(ast.args)):
            argTyp = self.visit(ast.args[i], param)
            paramTyp = func.param[i]
            if isinstance(argTyp , Zcode):
                ast.args[i].typ = argTyp
            elif not self.comparType(argTyp , paramTyp):
                raise TypeMismatchInStatement(ast)
        
        if func.typ is None:
            func.typ = VoidType()
        elif not self.comparType(func.typ , VoidType()):
            raise TypeMismatchInStatement(ast)
        
        return func.typ
    

    # class CallExpr(Expr): name: Id , args: List[Expr]
    def visitCallExpr(self, ast, param): 
        func = self.listFunction[0].get(ast.name.name)
        
        if not func : 
            Undeclared(Function() , ast.name.name)
        
        if len(ast.args) != len(func.param):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(ast.args)):
            argTyp = self.visit(ast.args[i], param)
            paramTyp = func.param[i]
            if isinstance(argTyp , Zcode):
                ast.args[i].typ = argTyp
            elif not self.comparType(argTyp , paramTyp):
                raise TypeMismatchInExpression(ast)
        
        if func.typ is None:
            return func
        
        elif self.comparType(func.typ , VoidType()):
            raise TypeMismatchInExpression(ast)
        
        return func.typ
    
    
    # class Block(Stmt): stmt: List[Stmt]  
    def visitBlock(self, ast, param): 
        for item in ast.stmt:
            
            if type(item) is Block:  
                self.visit(item, [{}] + param)
            else: 
                self.visit(item, param)


    # class For(Stmt): name: Id , condExpr: Expr , updExpr: Expr , body: Stmt
    def visitFor(self, ast, param):
        
        forEleTyp = [self.visit(ast.name , param) , self.visit(ast.condExpr , param) , self.visit(ast.updExpr , param)]

        for i in range(0, 3):
            if isinstance(forEleTyp[i] , Zcode):
                forEleTyp[i].typ = BoolType() if i == 1 else NumberType()
            elif not self.comparType(forEleTyp[i], BoolType() if i == 1 else NumberType()):
                raise TypeMismatchInStatement(ast)
            
        self.BlockFor += 1 
        self.visit(ast.body, [{}] + param)
        self.BlockFor -= 1  
      
        
    def visitContinue(self, ast, param):
        if self.BlockFor == 0: 
            raise MustInLoop(ast)


    def visitBreak(self, ast, param):
        if self.BlockFor == 0: 
            raise MustInLoop(ast)


    def visitNumberType(self, ast, param): return NumberType()
    def visitBoolType(self, ast, param): return BoolType()
    def visitStringType(self, ast, param): return StringType()
    def visitArrayType(self, ast, param): return ArrayType()
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()
    
    
    # class ArrayLiteral(Literal): value: List[Expr]
    def visitArrayLiteral(self, ast, param):
        
        for exp in ast.value:
            self.visit(exp, param)
            
        typ = self.visit(ast.value[0], param)
        if type(typ) in [StringType, BoolType, NumberType]:
            return ArrayType([len(ast.value)], typ)
        
        return ArrayType([len(ast.value)] + typ.size, typ.eleType)
        
     
    # class BinaryOp(Expr):op: str, left: Expr,  right: Expr
    def visitBinaryOp(self, ast, param):
 
        left_type = self.visit(ast.left, param)
        right_type = self.visit(ast.right, param)
        
        def check_types(expected_type):
            if isinstance(left_type, Zcode): 
                left_type.typ = expected_type
            if isinstance(right_type, Zcode):
                right_type.typ = expected_type
                
            left_type_cmp = self.comparType(self.visit(ast.left, param) , expected_type)
            right_type_cmp = self.comparType(self.visit(ast.right, param) , expected_type)
            
            if not left_type_cmp or not right_type_cmp:
                raise TypeMismatchInExpression(ast)
                
       
        if ast.op in ['+', '-', '*', '/', '%']:
            check_types(NumberType())
            return NumberType()
        
       
        elif ast.op in ['=', '!=', '<', '>', '>=', '<=']:
            check_types(NumberType())
            return BoolType()
        
         
        elif ast.op in ['and', 'or']:
            check_types(BoolType())
            return BoolType()
        
        
        elif ast.op == '==':
            check_types(StringType())
            return BoolType()
        
        
        elif ast.op == '...':
            check_types(StringType())
            return StringType()
        
        return Zcode() 


    # class UnaryOp(Expr): op: str, operand: Expr
    def visitUnaryOp(self, ast, param):
      
        operandExpr = self.visit(ast.operand , param)
        
        if ast.op in ["+" , "-"]:
            if isinstance(operandExpr, Zcode):
                operandExpr.typ = NumberType()
            elif not self.comparType(operandExpr , NumberType()):
                raise TypeMismatchInExpression(ast)
            
            return NumberType()
 
        elif ast.op in ["not"]:
            if isinstance(operandExpr, Zcode):
                operandExpr.typ = BoolType()
            elif not self.comparType(operandExpr , BoolType()):
                raise TypeMismatchInExpression(ast)

            return BoolType()
   
        
    # class ArrayCell(LHS): arr: Expr , idx: List[Expr]
    def visitArrayCell(self, ast, param):
        arrExpr = self.visit(ast.arr , param)
        
        # chua suy dien kieu cho array type
        if not isinstance(arrExpr , ArrayType):
            raise TypeMismatchInExpression(ast)
        
        for id in ast.idx:
            idTyp = self.visit(id , param)
            if isinstance(idTyp , Zcode):
                idTyp.typ = NumberType()
            elif not self.comparType(idTyp , NumberType()):
                raise TypeMismatchInExpression(ast)
      
        noDimen = len(arrExpr.size)
        noAccessDimen = len(ast.idx)
        
        if noDimen < noAccessDimen:
            raise TypeMismatchInExpression(ast)
        
        elif noDimen == noAccessDimen:
            return arrExpr.eleType
        
        elif noDimen > noAccessDimen:
            return ArrayType(arrExpr.size[noAccessDimen:] , arrExpr.eleType)
              
    

    # class If(Stmt) expr: Expr , thenStmt: Stmt , elifStmt: List[Tuple[Expr, Stmt]] , elseStmt: Stmt = None   
    def visitIf(self, ast, param):
        ifExpr = self.visit(ast.expr, param)
        if isinstance(ifExpr , Zcode):
            ifExpr.typ = BoolType()
        elif not self.comparType(ifExpr, BoolType()):
            raise TypeMismatchInStatement(ast) 
        
        self.visit(ast.thenStmt , [{}] + param)
        
        if ast.elifStmt:
            for elifTuple in ast.elifStmt:
                (cond, stmt) = elifTuple
                if isinstance(cond , Zcode):
                    cond.typ = BoolType()
                elif not self.comparType(self.visit(cond , param) , BoolType()):
                    raise TypeMismatchInStatement(ast)
                
                self.visit(stmt , [{}] + param)
        
        if ast.elseStmt: 
            self.visit(ast.elseStmt , [{}] + param)
        

    # class Assign(Stmt): lhs: Expr , exp: Expr
    def visitAssign(self, ast, param):
        leftTyp = self.visit(ast.lhs , param)
        rightTyp = self.visit(ast.rhs , param)
    
        if isinstance(leftTyp , Zcode) and isinstance(rightTyp , Zcode):
            raise TypeCannotBeInferred(ast)
        elif isinstance(leftTyp , Zcode):
            leftTyp.typ = rightTyp
        elif isinstance(rightTyp , Zcode):
            rightTyp.typ = leftTyp
        elif not self.comparType(leftTyp , rightTyp):
            raise TypeMismatchInStatement(ast)

    # class Return(Stmt): expr: Expr = None   
    def visitReturn(self, ast, param):
        self.Return = True
        
        returnExp = self.visit(ast.expr , param) if ast.expr else VoidType()
        func = self.function.typ if self.function.typ else self.function
        
        if isinstance(func , Zcode) and isinstance(returnExp, Zcode):
            raise TypeCannotBeInferred(ast) 
        
        elif isinstance(func , Zcode):
            func.typ = returnExp
        elif isinstance(returnExp , Zcode):
            returnExp.typ = func
        elif not self.comparType(returnExp, func):
            raise TypeMismatchInStatement(ast)