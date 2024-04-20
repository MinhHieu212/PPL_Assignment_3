
#  Student's name: Trần Minh Hiếu
#  Student ID: 2113363

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class Zcode: pass


class VarZcode(Zcode):              # Using for VarDecl 
    def __init__(self, typ = None):
        self.typ = typ              # Type
        
        
class ArrayZcode(Type):             # Using for VarDecl in case ArrayType
    def __init__(self, eleType):
        self.eleType = eleType      # list[Type]
        

class FuncZcode(Zcode):             # Using for FuncDecl 
    def __init__(self, param = [], typ = None, body = False):
        self.param = param          # list[Type]
        self.typ = typ              # Type
        self.body = body            # Bool , using to check part declaration
        

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
    
    
    # LHS , RHS : Type ( String , Boolean , Number , ArrayType , Zcode[FuncZcode,VarZcode] , ArrayZcode )
    def comparType(self, LHS, RHS): 
        if (type(LHS) is ArrayType) and (type(RHS) is ArrayType):
            if type(LHS.eleType) != type(RHS.eleType) or (len(LHS.size) != len(RHS.size)):
                return False
            
            for i in range(0, len(LHS.size)):
                if LHS.size[i] != RHS.size[i]:
                    return False
            
            return True
                
        return type(LHS) == type(RHS)
        
        
    # LHS , RHS : List[Type]     
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

            elif isinstance(left, Zcode) and isinstance(right, ArrayZcode):
                raise TypeCannotBeInferred(ast)

            elif isinstance(right, ArrayZcode):
                if isinstance(left, (StringType, BoolType, NumberType)):
                    raise TypeMismatchInStatement(ast)
                
                elif not self.setTypeArray(left, right):
                    raise TypeMismatchInStatement(ast)

            elif isinstance(left, Zcode):
                left.typ = right

            elif isinstance(right, Zcode):
                right.typ = left

            else:
                if not self.comparType(left, right):
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
        functionExist = self.listFunction[0].get(ast.name.name)
         
        if not functionExist:
            self.listFunction[0][ast.name.name] = FuncZcode(typeParam , None , ast.body)
        else: 
            if functionExist.body:
                raise Redeclared(Function() , ast.name.name)
            
            elif not ast.body:
                raise Redeclared(Function() , ast.name.name)
            
            elif not self.comparListType(typeParam , functionExist.param):
                raise Redeclared(Function() , ast.name.name)

            self.listFunction[0][ast.name.name].body = True 
        
        if ast.body: 
            self.function = self.listFunction[0].get(ast.name.name)
            # self.visit(ast.body ,  listParam + param)
            self.visit(ast.body , [{}] + listParam + param)
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
     
     
    # class BinaryOp(Expr):op: str, left: Expr, right: Expr
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
        
        # How to inffer for array Zcode -> ArrayType(? Dim , ? eleTyp)
        # Duy nói nếu pt được type của eleType thì oke , không thì Type can not be inffer
        # if isinstance(arrExpr , Zcode):
        #     arrExpr.typ = ArrayType()  
            
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
        
        
    def visitNumberType(self, ast, param): return NumberType()
    def visitBoolType(self, ast, param): return BoolType()
    def visitStringType(self, ast, param): return StringType()
    def visitArrayType(self, ast, param): return ArrayType()
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()

    
    # typeArray : ArrayType , typeArrayZcode : ArrayZcode 
    # typeArray: ArrayType([4,2] , NumerType()) and ArrayZcode: [Zcode , VarZcode , FuncZcode , [Zcode , Zcode]] => OKE
    def setTypeArray(self, typeArray, typeArrayZcode):
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False

        if len(typeArray.size) == 1:
            # Case: array of primitive types (1D array)
            for i in range(len(typeArrayZcode.eleType)):
                if isinstance(typeArrayZcode.eleType[i], Zcode):
                    typeArrayZcode.eleType[i].typ = typeArray.eleType
                    
                elif isinstance(typeArrayZcode.eleType[i], ArrayZcode):
                    return False  # Cannot assign a multi-dimensional array to a 1D array

        else:
            # Case: array of array types (multi-dimensional array)
            for i in range(len(typeArrayZcode.eleType)):
                if isinstance(typeArrayZcode.eleType[i], Zcode):
                    typeArrayZcode.eleType[i].typ = ArrayType(typeArray.size[1:], typeArray.eleType)
                    
                elif isinstance(typeArrayZcode.eleType[i], ArrayZcode):
                    if not self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType), typeArrayZcode.eleType[i]):
                        return False

        return True
    
    
    # class ArrayLiteral(Literal): value: List[Expr]
    # [[[Zcode, Zcode] , [Zcode , 1]] , [Zcode , [Zcode , Zcode]]] 
    # [[[Zcode, Zcode] , [Zcode , 1]] , [Zcode , [Zcode , "1"]]] 
    def visitArrayLiteral(self, ast, param):
        typ = None
        for item in ast.value:
            checkTyp = self.visit(item, param)  # đệ quy tại đây nếu như multi-dimensional
            if not (isinstance(checkTyp, Zcode) or isinstance(checkTyp, ArrayZcode)):
                typ = checkTyp
                break
            
        # Case 1: typ is None, meaning all elements are Zcode or ArrayZcode
        if typ is None:
            # [Zcode , Zcode , [Zcode , Zcode]] 
            eleTyp = []
            for item in ast.value:
                itemTyp = self.visit(item, param)
                if isinstance(itemTyp, Zcode):
                    eleTyp.append(itemTyp)
                else:
                    eleTyp.append(ArrayZcode(itemTyp.eleType))
            # Trả về cho Assign , VarDecl , Return , Param của Function để có thể suy diễn được kiểu của ArrayLiteral 
            return ArrayZcode(eleTyp)
          
        # Case 2: typ is a primitive type (StringType, BoolType, NumberType)
        elif type(typ) in [StringType, BoolType, NumberType]:    
            # [Zcode , Zcode , Zcode , NumberType()] 
            for item in ast.value:
                itemTyp = self.visit(item, param)
                if isinstance(itemTyp, Zcode):
                    itemTyp.typ = typ
                elif isinstance(itemTyp, ArrayZcode) or not self.comparType(itemTyp, typ):
                    raise TypeMismatchInExpression(ast)
            
            return ArrayType([len(ast.value)] , typ)
            
        # Case 3: typ is an ArrayType
        else:
            # ArrayType([2, 1] , NumberType())
            # [Zcode , Zcode , [[NumberType()] , [NumberType()]] , [[Zcode] , Zcode]] => Oke
            # [Zcode , [Zcode , Zcode] , [[NumberType()] , [NumberType()]] , [[StringType()] , Zcode]] => Error
            for item in ast.value:
                itemTyp = self.visit(item, param)
                if isinstance(itemTyp, Zcode):
                    itemTyp.typ = typ
                    
                elif isinstance(itemTyp, ArrayZcode):
                    if not self.setTypeArray(typ , itemTyp):
                        raise TypeMismatchInExpression(ast)
                    
                else: # itemTyp is arrayType
                    if not self.comparType(typ , itemTyp):
                        raise TypeMismatchInExpression(ast)

            return ArrayType([len(ast.value)] + typ.size , typ.eleType)
                 
         
    # class Return(Stmt): expr: Expr = None   
    def visitReturn(self, ast, param):
        self.Return = True
        exprType = self.visit(ast.expr , param) if ast.expr else VoidType()
        funcType = self.function.typ if self.function.typ else self.function
        
        if isinstance(funcType , (Zcode, ArrayZcode)) and isinstance(exprType , (Zcode, ArrayZcode)):
            raise TypeCannotBeInferred(ast) 
        
        elif isinstance(funcType, Zcode):
            if type(exprType) in [StringType, BoolType, NumberType, ArrayType, VoidType]:
                funcType.typ = exprType
            else:
                raise TypeMismatchInStatement(ast)
                
        elif isinstance(funcType, ArrayZcode):
            if type(exprType) is ArrayType:
                if not self.setTypeArray(exprType , funcType):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
                
        elif isinstance(exprType, Zcode):
            if type(funcType) in [StringType, BoolType, NumberType, ArrayType]:
                exprType.typ = funcType
            else:
                raise TypeMismatchInStatement(ast)
                
        elif isinstance(exprType, ArrayZcode):
            if type(funcType) is ArrayType:
                if not self.setTypeArray(funcType , exprType):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
            
        elif not self.comparType(exprType, funcType):
            raise TypeMismatchInStatement(ast)
        
        
    # class CallStmt(Stmt): name: Id {name : str} , args: List[Expr] 
    def visitCallStmt(self, ast, param):
        func = self.listFunction[0].get(ast.name.name)
        
        if not func: 
            raise Undeclared(Function() , ast.name.name)
        
        if len(ast.args) != len(func.param):
            raise TypeMismatchInStatement(ast)
        
        for i in range(len(ast.args)):
            functionParamType = func.param[i]
            passedArgumentType  = self.visit(ast.args[i], param)
            
            if isinstance(passedArgumentType , Zcode):
                if type(functionParamType) in [StringType, BoolType, NumberType, ArrayType]:
                    passedArgumentType.typ = functionParamType
                else:
                    raise TypeMismatchInStatement(ast)
                
            elif isinstance(passedArgumentType , ArrayZcode):
                if type(functionParamType) is ArrayType:
                    if not self.setTypeArray(functionParamType , passedArgumentType):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
                
            elif not self.comparType(passedArgumentType , functionParamType):
                raise TypeMismatchInStatement(ast)
        
        if func.typ is None:
            func.typ = VoidType()
            
        elif not self.comparType(func.typ , VoidType()):
            raise TypeMismatchInStatement(ast)
        
        return func.typ
    

    # class CallExpr(Expr): name: Id , args: List[Expr]
    def visitCallExpr(self, ast, param): 
        func = self.listFunction[0].get(ast.name.name)
        
        if not func: 
            Undeclared(Function() , ast.name.name)
        
        if len(ast.args) != len(func.param):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(ast.args)):
            functionParamType = func.param[i]
            passedArgumentType  = self.visit(ast.args[i], param)
            
            if isinstance(passedArgumentType , Zcode):
                if type(functionParamType) in [StringType, BoolType, NumberType, ArrayType]:
                    passedArgumentType.typ = functionParamType
                else:
                    raise TypeMismatchInExpression(ast)
                
            elif isinstance(passedArgumentType , ArrayZcode):
                if type(functionParamType) is ArrayType:
                    if not self.setTypeArray(functionParamType , passedArgumentType):
                        raise TypeMismatchInExpression(ast)
                else:
                    raise TypeMismatchInExpression(ast)
                
            elif not self.comparType(passedArgumentType , functionParamType):
                raise TypeMismatchInExpression(ast)
        
        if func.typ is None:
            return func
        
        elif self.comparType(func.typ , VoidType()):
            raise TypeMismatchInExpression(ast)
        
        return func.typ
        
    # class Assign(Stmt): lhs: Expr , exp: Expr
    def visitAssign(self, ast, param):
        leftTyp = self.visit(ast.lhs, param)
        rightTyp = self.visit(ast.rhs, param)

        if isinstance(leftTyp, Zcode) and isinstance(rightTyp, Zcode):
            raise TypeCannotBeInferred(ast)
        
        elif isinstance(leftTyp, Zcode):
            leftTyp.typ = rightTyp
        elif isinstance(rightTyp, Zcode):
            rightTyp.typ = leftTyp
        elif isinstance(leftTyp, ArrayType) and isinstance(rightTyp, ArrayZcode):
            if not self.setTypeArray(leftTyp, rightTyp):
                raise TypeMismatchInStatement(ast) 
            
        elif isinstance(leftTyp, ArrayZcode) and isinstance(rightTyp, ArrayType):
            if not self.setTypeArray(rightTyp, leftTyp):
                raise TypeMismatchInStatement(ast)
            
        elif not self.comparType(leftTyp, rightTyp):
            raise TypeMismatchInStatement(ast)