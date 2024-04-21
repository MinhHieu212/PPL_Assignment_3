"""
^name : Võ Tiến
^FB : https://www.facebook.com/profile.php?id=100056605580171
^GROUP: https://www.facebook.com/groups/211867931379013/
^DAY : 15/4/2024
"""

from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body
    def __str__(self):
        return f"FuncZcode(param=[{', '.join(str(i) for i in self.param)}],typ={str(self.typ)},body={self.body})"

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    
    def __str__(self):
        return f"VarZcode(type={self.typ})"

class ArrayZcode(Type):
    def __init__(self, eleType):
        self.eleType = eleType
    def __str__(self):
        return f"ArrayZcode(eleType=[{', '.join(str(i) for i in self.eleType)}])"
    
class CannotBeInferredZcode(Type):
    def __str__(self):
        return "CannotBeInferredZcode()"

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.ast = ast 
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = {
            "readNumber" : FuncZcode([], NumberType(), True),
            "readBool" : FuncZcode([], BoolType(), True),
            "readString" : FuncZcode([], StringType(), True),
            "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
            "writeBool" : FuncZcode([BoolType()], VoidType(), True),
            "writeString" : FuncZcode([StringType()], VoidType(), True)
        }
    
    def print(self):
        print(f"BlockFor {self.BlockFor}")
        print(f"function {str(self.function)}")
        print(f"Return {self.Return}")
        print(f"listFunction :")
        for key, value in self.listFunction.items():
            print(f"    {key}  {str(value)}")       
    
    def check(self):
        self.visit(self.ast, [{}])
        return None

    def LHS_RHS_stmt(self,LHS : Type, RHS : Type, ast):
        # print(f"LHS_RHS_stmt {LHS} {RHS}")
        #! ĐỌC TRONG DISCORD
        
    def LHS_RHS_expr(self, LHS : Type, RHS : Type,ast) -> bool:
        # print(f"LHS_RHS_EXPR {LHS} {RHS}")
        #! ĐỌC TRONG DISCORD

    def comparType(self, LHS : Type, RHS : Type) -> bool:
    """_comparListType
        #* LHS và RHS chỉ có thể list các type sau Void, number, string, bool, arrayType
        #* TH1 nếu LHS và RHS khác kích thước -> Flase
        #* duyệt từng phần tử gọi self.comparType(LHS[i], RHS[i])
    """    
    
    def setTypeArray(self, typeArray, typeArrayZcode):
        #* Trường hợp size khác nhau
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False
        
        #* trường hợp bên trong array là các kiểu nguyên thủy (array 1 chiều)
           #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = typeArray.eleType
           #^ nếu    là arrayZcode : trả về False (vì 1 chiều mà bắt gán 2 chiều :) )
        """_VD 
            typeArray = arrayType([3], StringType), typeArrayZcode = ArrayZcode([VarZcode('a'), FuncZcode('foo'), ArrayZcode([VarZcode('b')])])
            index = 0 -> VarZcode('a').type = StringType
            index = 1 -> FuncZcode('foo').type = StringType
            index = 2 -> ArrayZcode([VarZcode('b')]) ->  fail -> return Flase
        """
        if len(typeArray.size) == 1:
            #TODO implement
            pass
            
        #* trường hợp bên trong array là các arrayType (array >= 2 chiều)
           #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = ArrayType(typeArray.size[1:], typeArray.eleType)
           #^ nếu typeArrayZcode.eleType[i] là arrayZcode : gọi đệ quy self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType),typeArrayZcode[i]) để vào bên trong xem có lỗi gì không       
        """_VD 
            typeArray = arrayType([2,3], StringType), typeArrayZcode = ArrayZcode([VarZcode('a'), FuncZcode('foo'), ArrayZcode([VarZcode('b')])])
            index = 0 -> VarZcode('a').type = arrayType([3], StringType)
            index = 1 -> FuncZcode('foo').type = arrayType([3], StringType)
            index = 2 -> đệ quy typeArray = arrayType([3], StringType), typeArrayZcode = ArrayZcode([VarZcode('b')])
                vì typeArray  có 3 phần tử mà typeArrayZcode chỉ có 1 phần tử -> return false
        """
        else:
            #TODO implement

    def visitProgram(self, ast, param):
        for i in ast.decl: self.visit(i, param)
        
        #TODO implement dùng for duyệt qua self.listFunction nếu item[i].body == Flase thì nén ra lỗi

        
        #TODO implement kiểm tra main có None hay không, main.param có rỗng hay không, main.typ có phải là VoidType hay không

        
    def visitVarDecl(self, ast, param):
        #TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared
        if param[0].get(ast.name.name): raise Redeclared(Variable(), ast.name.name)
        
        param[0][ast.name.name] = VarZcode(ast.varType)
        
        if ast.varInit:
            #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng

    def visitFuncDecl(self, ast, param):
        method = self.listFunction.get(ast.name.name)
        #TODO kiểm tra name có trong self.listFunction hay không nén ra lỗi Redeclared

        #^th1: KHAI BÁO TRƯỚC 1 PHẦN KHÔNG CÓ BODY
        if ast.body is None:
            typeParam = [] #! tìm ra listtype
            #TODO: implement 
            
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, False)
            return

         
        listParam = {} #! dạng Dict có name khi visit dùng self.visit(ast.body, [listParam] + param)
        typeParam = [] #! dạng mảng không cần name truyền agrc vào FuncZcode
        #TODO: implement

        #^TH2 khai báo 1 phần trước rồi lần này khai báo có body
        if method:
            ListLHS = self.listFunction[ast.name.name].param
            ListRHS = typeParam
            #TODO: implement kiểm tra 2 dánh sách có giống nhau không -> Redeclared(Function(), ast.name.name) 
=
            self.listFunction[ast.name.name].body = True
        else:
            self.listFunction[ast.name.name] = FuncZcode(typeParam, None, True)
        
        self.Return = False
        self.function = self.listFunction[ast.name.name] 
        self.visit(ast.body, [listParam] + param)
        if not self.Return:
            if self.listFunction[ast.name.name].typ is None: 
                self.listFunction[ast.name.name].typ = VoidType()
            elif not isinstance(self.listFunction[ast.name.name].typ, VoidType):
                raise TypeMismatchInStatement(Return(None))
                
 
    def visitId(self, ast, param):
        """
            # TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
                #^ đối với giá trị trả về nếu Id.typ = None thì trả về chính nó luôn Id, nếu cso Id.typ thì trả về typ của nó
                #^ return Id.typ if Id.typ else Id (trả cơ chế reference hay con trỏ)
                #^ https://www.geeksforgeeks.org/references-in-cpp/
            Vd reference:
                def visitId() :
                    param = [{'a' : VarZcode(None)}]
                    id = param[0].get('a')
                    return Id.typ if Id.typ else Id
                
                x = visitId() # lúc này x với VarZcode(None) là như 1
                x.typ = NumberType
                -> có thể hiểu param = [{'a' : VarZcode(None)}] chuyển thành param = [{'a' : VarZcode(NumberType)}]         
        """


    def visitCallExpr(self, ast, param):
        method = self.listFunction.get(ast.name.name)
        #TODO: implement kiểm tra Undeclared
        
        #TODO: implement kiểm tra kích thước method.param và ast.args -> TypeMismatchInStatement
        for i in range(len(method.param)):
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
        
        #TODo: implement nếu method.typ là voidtype -> TypeMismatchInExpression, nếu không thì trả về theo nguyên lí giống ID trên
       

    def visitCallStmt(self, ast, param):
        method = self.listFunction.get(ast.name.name)
        #TODO: implement kiểm tra Undeclared
        
        #TODO: implement kiểm tra kích thước method.param và ast.args -> TypeMismatchInStatement
        for i in range(len(method.param)):
            #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
    
        #TODO: implement nếu method.typ là None thì gán Voidtype, nếu không thì kiểm tra có phải voidtype hay không nén ra lỗi TypeMismatchInStatement
        

    def visitIf(self, ast, param):
        """_typExpr_"""   
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
        self.visit(ast.thenStmt, param)    
        
        """_elifStmt_"""   
        for item in ast.elifStmt:
            #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng 
            self.visit(item[1], param)           

        """_elseStmt_
        """            
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, param)
        
    def visitFor(self, ast, param):
        # name: Id
        # condExpr: Expr
        # updExpr: Expr
        # body: Stmt
        """_typID_"""        
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng       
        
        """_typCondExpr_"""    
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng  

        """_typUpdExpr_"""            
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
        
        
        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, param)
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
    
    def visitReturn(self, ast, param):
        self.Return = True
        #TODO: 3

    def visitAssign(self, ast, param):
        #TODO: implement Nguyên lí LHS và RHS cho stmt chỉ 3 hàng
            
    def visitBinaryOp(self, ast, param):
        op = ast.op
        if op in ['+', '-', '*', '/', '%']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
        elif op in ['and', 'or']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
        elif op in ['==']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
        elif op in ['...']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
        
        

        """_right_        
            TƯƠNG TỰ LEFT     
        """        
        if op in ['+', '-', '*', '/', '%']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            #TODO: implement trả về type
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            #TODO: implement trả về type
        elif op in ['and', 'or']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            #TODO: implement trả về type
        elif op in ['==']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            #TODO: implement trả về type
        elif op in ['...']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            #TODO: implement trả về type

    def visitUnaryOp(self, ast, param):
        op = ast.op
        if op in ['+', '-']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            #TODO: implement trả về type
        if op in ['not']:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            #TODO: implement trả về type
            
    def visitArrayCell(self, ast, param):
        arr = self.visit(ast.arr, param)
        if isinstance(arr, (BoolType, StringType, NumberType)):
            raise TypeMismatchInExpression(ast)
        elif not isinstance(arr, ArrayType):
            return CannotBeInferredZcode()

        for item in ast.idx:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng
            
        if len(arr.size) < len(ast.idx): raise TypeMismatchInExpression(ast)
        elif len(arr.size) == len(ast.idx): return arr.eleType
        return ArrayType(arr.size[len(ast.idx):], arr.eleType)   

    def visitArrayLiteral(self, ast, param):
        mainTyp = None
        for item in ast.value:
            checkTyp = self.visit(item, param)
            if mainTyp is None and isinstance(checkTyp, (BoolType, StringType, NumberType, ArrayType)):
                mainTyp = checkTyp
            elif isinstance(checkTyp, CannotBeInferredZcode):
                return CannotBeInferredZcode()
        
        #^ TH1 : mainTyp is None nghĩa là trong array chỉ gồm Zcode và ArrayZcode nên return ArrayZcode
        if mainTyp is None:
            #TODO: implement < 3 dòng 
        
        for item in ast.value:
            #TODO: implement Nguyên lí LHS và RHS cho expr chỉ 4 hàng

        
        #^ TH đầu tiên main là BoolType, StringType, NumberType
            #! trả về array có eleType là mainTyp và size là kích thước của ast.value
        #^ TH hai main là mảng
            #! trả về array có eleType là mainTyp.eleType và size là kích thước của [float(len(ast.value))] + mainTyp.size
        #TODO: implement
            
        
            
    """phần này sẽ là cố định do ngắn quá :(( """
    def visitBlock(self, ast, param):
        paramNew = [{}] + param #! tăng tầm vực
        for item in ast.stmt: 
            self.visit(item,paramNew)   
    def visitContinue(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)
    def visitBreak(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)   
    def visitNumberType(self, ast, param): return ast
    def visitBoolType(self, ast, param): return ast
    def visitStringType(self, ast, param): return ast
    def visitArrayType(self, ast, param): return ast
    def visitNumberLiteral(self, ast, param): return NumberType()
    def visitBooleanLiteral(self, ast, param): return BoolType()
    def visitStringLiteral(self, ast, param): return StringType()

        
        





