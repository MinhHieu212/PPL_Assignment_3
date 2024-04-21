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
    def __str__(self):
        return f"VarZcode(type={self.typ})"   
       
        
class ArrayZcode(Type):             # Using for VarDecl in case ArrayType
    def __init__(self, eleType):
        self.eleType = eleType      # list[Type]
    def __str__(self):
        return f"ArrayZcode(eleType=[{', '.join(str(i) for i in self.eleType)}])"    


class FuncZcode(Zcode):             # Using for FuncDecl 
    def __init__(self, param = [], typ = None, body = False):
        self.param = param          # list[Type]
        self.typ = typ              # Type
        self.body = body            # Bool , using to check part declaration
    def __str__(self):
        return f"FuncZcode(param=[{', '.join(str(i) for i in self.param)}],typ={str(self.typ)},body={self.body})"    


class CannotBeInferredZcode(Type):
    def __str__(self):
        return "CannotBeInferredZcode()"


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
       
       
    def print(self):
        print(f"BlockFor {self.BlockFor}")
        print(f"function {str(self.function)}")
        print(f"Return {self.Return}")
        print(f"listFunction :")
        for key, value in self.listFunction.items():
            print(f"    {key}    {str(value)}") 
       
       
    def check(self):
        self.visit(self.ast, [{}])
        return None    
    
    
    def LHS_RHS_stmt(self, LHS: Type, RHS: Type, ast):
        # print(f"LHS_RHS_stmt {LHS} {RHS}")
        if isinstance(LHS, CannotBeInferredZcode) or isinstance(RHS, CannotBeInferredZcode):
            # print("111111111111 LHS_RHS_stmt 111111111111")
            raise TypeCannotBeInferred(ast)

        elif isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            # print("2222222222 LHS_RHS_stmt 2222222222")
            raise TypeCannotBeInferred(ast)

        elif isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            # print("3333333333 LHS_RHS_stmt 3333333333")
            raise TypeCannotBeInferred(ast)

        elif isinstance(LHS, ArrayType) and isinstance(RHS, ArrayZcode):
            if not self.setTypeArray(LHS, RHS):
                # print("444444444444 LHS_RHS_stmt 444444444444")
                raise TypeMismatchInStatement(ast)

        elif isinstance(RHS, ArrayZcode):
            # print("5555555555555555 LHS_RHS_stmt 5555555555555555")cl
            raise TypeCannotBeInferred(ast)

        elif isinstance(LHS, Zcode):
            LHS.typ = RHS

        elif isinstance(RHS, Zcode):
            RHS.typ = LHS
            
        elif not self.comparType(LHS.typ if isinstance(LHS, Zcode) and LHS.typ else LHS , RHS.typ if isinstance(RHS, Zcode) and RHS.typ else RHS):
            # print("77777777777777 LHS_RHS_stmt 77777777777777")
            raise TypeMismatchInStatement(ast)

      
    def LHS_RHS_expr(self, LHS : Type, RHS : Type,ast) -> bool:
        # print(f"LHS_RHS_expr {LHS} {RHS}")
        if isinstance(LHS, CannotBeInferredZcode) or isinstance(RHS, CannotBeInferredZcode):
            return True
        
        elif isinstance(LHS, Zcode) and isinstance(RHS, Zcode):
            return True
        
        elif isinstance(LHS, Zcode) and isinstance(RHS, ArrayZcode):
            return True
        
        elif isinstance(LHS, ArrayType) and isinstance(RHS, ArrayZcode):
            if not self.setTypeArray(LHS, RHS):
                raise TypeMismatchInExpression(ast)
        
        elif isinstance(RHS, ArrayZcode):
            return True
        
        elif isinstance(LHS, Zcode):
            LHS.typ = RHS 
            
        elif isinstance(RHS, Zcode):
            RHS.typ = LHS
        
        elif not self.comparType(LHS.typ if isinstance(LHS, Zcode) and LHS.typ else LHS , RHS.typ if isinstance(RHS, Zcode) and RHS.typ else RHS):
            raise TypeMismatchInExpression(ast)
        
        return False
    
    
    # LHS , RHS : Type ( String , Boolean , Number , ArrayType , Zcode[FuncZcode,VarZcode] , ArrayZcode)
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
            LHS = param[0][ast.name.name].typ if param[0][ast.name.name].typ else param[0][ast.name.name]
            RHS = self.visit(ast.varInit, param)
            self.LHS_RHS_stmt(LHS, RHS, ast)


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
            LHS = forEleTyp[i]
            RHS  = BoolType() if i == 1 else NumberType()
            self.LHS_RHS_stmt(LHS, RHS, ast)
            
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
        op = ast.op
        left = self.visit(ast.left, param)
       
        if op in ['+', '-', '*', '/', '%']:
            LHS = NumberType()
            RHS = left  
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            LHS = self.visit(ast.left, param)
            RHS = self.visit(ast.right, param)  
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            return NumberType()

        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            LHS = NumberType()
            RHS = left  
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            LHS = self.visit(ast.left, param)
            RHS = self.visit(ast.right, param)    
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            return BoolType()

        elif op in ['and', 'or']:
            LHS = BoolType()
            RHS = left  
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            LHS = self.visit(ast.left, param)
            RHS = self.visit(ast.right, param)   
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            return BoolType()

        elif op == '==':
            LHS = StringType()
            RHS = self.visit(ast.right, param)  
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            LHS = self.visit(ast.left, param)
            RHS = self.visit(ast.right, param)  
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            return BoolType()

        elif op == '...':
            LHS = StringType()
            RHS = left  
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            LHS = self.visit(ast.left, param)
            RHS = self.visit(ast.right, param)    
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            return StringType()


    # class UnaryOp(Expr): op: str, operand: Expr
    def visitUnaryOp(self, ast, param):
        if ast.op in ["+" , "-"]:
            LHS = NumberType()
            RHS = self.visit(ast.operand , param)  
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            return NumberType()
        
        elif ast.op in ["not"]:
            LHS = BoolType()
            RHS = self.visit(ast.operand , param)  
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()

            return BoolType()
   
        
    # class ArrayCell(LHS): arr: Expr , idx: List[Expr]
    def visitArrayCell(self, ast, param):
        arrExpr = self.visit(ast.arr, param)
        if isinstance(arrExpr, (BoolType, StringType, NumberType)):
            raise TypeMismatchInExpression(ast)
        elif not isinstance(arrExpr, ArrayType):
            return CannotBeInferredZcode()

        for id in ast.idx:
            LHS = NumberType()
            RHS = self.visit(id, param)
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()
      
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
        LHS = BoolType()
        RHS = self.visit(ast.expr, param)
        self.LHS_RHS_stmt(LHS, RHS, ast)
        
        self.visit(ast.thenStmt , param)
         
        if ast.elifStmt:
            for elifTuple in ast.elifStmt:
                (expr, stmt) = elifTuple
                LHS = BoolType()
                RHS = self.visit(expr , param)
                self.LHS_RHS_stmt(LHS, RHS, ast)
                self.visit(stmt , param)
        
        if ast.elseStmt: 
            self.visit(ast.elseStmt , param)
        
        
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
            checkTyp = self.visit(item, param)  # Đệ quy tại đây nếu như multi-dimensional
            if typ is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
                typ = checkTyp
            elif isinstance(checkTyp, CannotBeInferredZcode):
                return CannotBeInferredZcode()
        
        
        # Case 1: typ is None, meaning all elements are Zcode or ArrayZcode
        if typ is None:
            eleTyp = []
            for item in ast.value:
                eleTyp.append(self.visit(item, param))
            return ArrayZcode(eleTyp)
          
        for item in ast.value:
            LHS = typ 
            RHS = self.visit(item, param)
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()
        
        if  isinstance(typ, (StringType, BoolType, NumberType)):    
            # Case 2: typ is a primitive type (StringType, BoolType, NumberType)
            return ArrayType([len(ast.value)] , typ)
        else:
            # Case 3: typ is an ArrayType
            return ArrayType([float(len(ast.value))] + typ.size , typ.eleType)
                 
         
    # class Return(Stmt): expr: Expr = None   
    def visitReturn(self, ast, param):
        self.Return = True
        LHS = self.function.typ if self.function.typ else self.function
        RHS = self.visit(ast.expr, param) if ast.expr else VoidType()
        self.LHS_RHS_stmt(LHS, RHS, ast)

        
    # class CallStmt(Stmt): name: Id {name : str} , args: List[Expr] 
    def visitCallStmt(self, ast, param):
        func = self.listFunction[0].get(ast.name.name)
        
        if not func: 
            raise Undeclared(Function() , ast.name.name)
        
        if len(ast.args) != len(func.param):
            raise TypeMismatchInStatement(ast)
       
        for i in range(len(ast.args)):
            LHS = func.param[i]
            RHS  = self.visit(ast.args[i], param)
            self.LHS_RHS_stmt(LHS, RHS, ast)
            
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
            LHS = func.param[i]
            RHS  = self.visit(ast.args[i], param)            
            cannotBeInferred = self.LHS_RHS_expr(LHS, RHS, ast)
            if cannotBeInferred: return CannotBeInferredZcode()
        
        if func.typ is None:
            return func
        
        elif self.comparType(func.typ , VoidType()):
            raise TypeMismatchInExpression(ast)
        
        return func.typ
        
    # class Assign(Stmt): lhs: Expr , exp: Expr
    def visitAssign(self, ast, param):
        LHS = self.visit(ast.lhs, param)
        RHS = self.visit(ast.rhs, param)
        self.LHS_RHS_stmt(LHS, RHS, ast)