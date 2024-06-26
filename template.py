"""
^NAME : Võ Tiến
^FB : https://www.facebook.com/profile.php?id=100056605580171
^GROUP: https://www.facebook.com/groups/211867931379013/
^DAY : 25/3/2024
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode:
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    
        
"""
Kiến thức cần 
List : https://www.w3schools.com/python/python_lists.asp
Dict : https://www.w3schools.com/python/python_dictionaries.asp
type() : https://www.w3schools.com/python/python_datatypes.asp
isinstance() : https://www.w3schools.com/python/ref_func_isinstance.asp
"""
"""
^NAME : Võ Tiến
^FB : https://www.facebook.com/profile.php?id=100056605580171
^GROUP: https://www.facebook.com/groups/211867931379013/
^DAY : 25/3/2024
"""

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast, ):
        self.ast = ast
        self.BlockFor = 0
        self.function = None #! hàm hiện tại đang được dùng để kiểm tra static
        self.Return = False #! kiểm tra hàm hiện tại có return hay không
        
        #! lưu danh sách các hàm dưới dạng Dict 
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
        #! so sánh 2 type có trùm nhau hay không
        #! so sánh nếu 2 type đều là array -> kiểm tra từng phần tử trong size có giống hay không về kích thước và giá trị bên trong
        #! nếu giống thì trả true, ngược lại false
        pass
    

    def comparListType(self, listLHS, listRHS):
        #! so sánh 2 list type gọi hàm comparType xử lí
        pass  
    
    
    def visitProgram(self, ast, param):
        #! duyệt qua các biến và hàm toàn cục
        for i in ast.decl: self.visit(i, param)
        #! sau bước này param có dạng [{biến toàn cục, hàm}]
        """
            TODO check No definition for a function in self.listFunction
            ^ gợi ý: duyệt tìm trong self.listFunction có FuncZcode nào có body = false hay không
            ví dụ 1 -> đúng
            func foo(number a)
            func foo(number a) return
            
            ví dụ 2 -> đúng
            func foo(number a) return
            
            ví dụ 3 -> sai  NoDefinition
            func foo(number a)
        """

        """
            TODO check No entry ponumber in self.listFunction
            ^ gợi ý: kiểm tra hàm main có trả về voidtype, không có param truyền vào hay không, có tồn tại main hay không
            ví dụ 1 -> đúng
            func main() return
            
            ví dụ 2 -> đúng
            func main()
            func main() begin
            end
             
            ví dụ 3 -> sai NoEntryPonumber
            func main(number a) return
            
            ví dụ 4 -> sai NoEntryPonumber
            func main() return 1       
            
            ví dụ 5 -> sai NoEntryPonumber
            không có hàm main      
        """        
        
  

    def visitVarDecl(self, ast, param):
        """
            TODO kiểm tra name có trong param[0] hay không nén ra lỗi Redeclared
            ^ gợi ý : tìm trong param[0] xem có tên trùm hay không
            ví dụ 1 -> đúng
            number a

            ví dụ 2 -> Redeclared(Variable(), ast.name.name
            number a
            string a    
            
            ví dụ 3 -> Redeclared(Variable(), ast.name.name)
            func a()
            number a
        """           
     
        
        
        """
            TODO kiểm tra TypeCannotBeInferred và TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
            ^ ý tưởng : visit RHS và LHS tìm được type (dùng isinstance)
            ^ có 2 loại là type bình thường (numbertype, stringtype, booleantype, arraytype) và type chưa xác định (FuncZcode, VarZcode)
            ^ TH1 : cả 2 đều trả về Zcode -> TypeCannotBeInferred -> cả 2 vế đều không suy diễn được
            ^ TH2, 3: nếu 1 trong 2 bên trả về Zcode bên kia xác định type thì gán type của Zcode với type đó -> suy diễn type của vế còn lại
            ^ TH4 : cả 2 đều có type nên kiểm tra xem 2 type có giống nhau không comparType -> TypeMismatchInStatement
            ví dụ 1 -> đúng
            number a <- 1 

            ví dụ 2 -> TH1 TypeCannotBeInferred
            func foo()
            var a <- foo()    
            
            ví dụ 3 -> TH3, 4 : foo().typ = b.typ = numberType()
            func foo()
            number a <- foo()
            var b <- a            

            ví dụ 4 -> TH4 TypeMismatchInStatement
            number a <- "1"                
        """ 


    def visitFuncDecl(self, ast, param):
        """
            TODO kiểm tra name có trong self.listFunction hay không nén ra lỗi Redeclared 
            ^ gợi ý : tìm trong self.listFunction xem có tên trùng hay không, kiểm tra luôn phần body để xác định có khai báo 1 phần hay không
            
            ví dụ 1 -> đúng
            func foo() return

            ví dụ 2 -> đúng
            func foo()
            func foo() return
            
            ví dụ 3 -> Redeclared
            func foo() return
            func foo()

            ví dụ 4 -> Redeclared
            func foo()
            func foo()
            
            ví dụ 5 -> Redeclared
            func foo() return
            func foo() return
        """ 
        
        listParam = {} #! dạng Dict có name khi visit dùng self.visit(ast.body, [listParam] + param)
        typeParam = [] #! dạng mảng không cần name truyền agrc vào FuncZcode
        
        """
            TODO kiểm tra ast.param trong hàm trong listParam giống phần vardecl -> nén ra lỗi Redeclared 
            ^ cập nhật listParam (giống param) và typeParam (chỉ gồm các type)
            ^ typeParam = [numberType, stringType, ...]
            ví dụ 1 -> đúng Redeclared
            func foo(number a, string a) return
        """ 

        
        self.Return = False #! kiểm tra hàm hiện tại có return hay không
        """
            TODO kiểm tra self.function = method hàm hiện tại chuẩn bị vào body nó xử lí
            ^ nhớ cập nhật self.function = self.listFunction[ast.name.name] -> xác định hàm hiện tại sẽ vào body của nó xử lí
            ^ TH1 : method đã tồn tại trước khi khai báo 1 phần (phần này đã có trong param) VD :
            func foo()
            func foo() begin -> đang xử lí bước này
            end
            
            ^ TH2 : method chưa tồn tại trước và khai báo 1 phần (phần này cập nhật trong param)
            func foo()
            
            ^ TH3 : method khai báo đầu đủ lần đầu không có khai báo 1 phần (phần này cập nhật trong param)
            func foo() begin
            end
            
            ^ Chú ý nếu mà có khai báo body TH1, TH3 -> khi về cuối mà type hàm không thay đổi thì gán về VoidType()
            func foo() begin 
            end     
            -> type foo là VoidType  
                 
            func foo() begin 
                return 1
            end     
            -> type foo là numberType
            ^ gợi ý : khi visit body thì thêm tầm vực mới là {listParam} -> self.visit(body, [{listParam}] + param)
        """
        #! hàm này không có return
        if not self.Return:
            #! type cũng chưa có luôn ta xác định nó VoidType
            if self.listFunction[ast.name.name].typ is None:
                self.listFunction[ast.name.name].typ = VoidType()
            #! type đã có so sánh nó với VoidType
            elif not self.comparType(self.listFunction[ast.name.name].typ, VoidType()): 
                raise TypeMismatchInStatement(Return(None))
        

    def visitId(self, ast, param):
        """
            TODO kiểm tra xem name có trong toàn bộ param nén lỗi Undeclared
            ^ nếu không Undeclared thì return về Id.typ nếu VarZcode.typ != None còn nếu VarZcode.typ = None thì return VarZcode
            ^ nguyên lí nó truyền theo con trỏ trong c++, nếu thay đổi VarZcode thì param cũng thay đổi
            VD 1:
            number a
            number b <- a -> a đã có VarZcode.typ nên return VarZcode.typ

            VD 2:
            number b <- a -> Undeclared(Identifier(), ast.name)      

            VD 3:
            var a
            number b <- a -> a có VarZcode.typ = None nên return VarZcode              
        """
   

    def visitCallExpr(self, ast, param):
        """
            TODO kiểm tra xem name có trong self.listFunction nén lỗi Undeclared
            VD 1: đúng 
            func foo()
            func main()begin
                var a <- foo()
            end
            
            VD 2: Undeclared
            func foo()
            func main()begin
                var a <- foo1()
            end
            
        """   
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ xét listLHS (là method.param) và listRHS (là ast.args)
                ^ nếu len khác nhau TypeMismatchInExpression
                ^ nếu self.comparType(LHS[i], RHS[i]) -> TypeMismatchInExpression
            ^ nếu FuncZcode.typ is None thì return FuncZcode
            ^ nếu comparType(FuncZcode.typ, VoidType()) -> TypeMismatchInExpression
            ^ còn lại return FuncZcode.typ (giống phần VarZcode)
        """   
       

    def visitCallStmt(self, ast, param):
        """như CallExpr chỉ khác ở chỗ not comparType(FuncZcode.typ, VoidType()) -> TypeMismatchInStatement"""
    

    def visitIf(self, ast, param):
        """
            TODO giống phần kiểm tra TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
            ^ ast.expr có LHS = BoolType(), RHS = self.visit(ast.expr, param)
            ^ body khi visit nhớ thêm 1 tầm vực mới
        """   
 
        
        """
            TODO giống phần kiểm tra TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
            ^ expr in ast.elifStmt có LHS = BoolType(), RHS = .... 
            ^ body khi visit nhớ thêm 1 tầm vực mới
        """   

        
        """
            TODO kiểm tra elseStmt
            ^ body khi visit nhớ thêm 1 tầm vực mới
        """           
     
    def visitFor(self, ast, param):
        """
            TODO giống phần kiểm tra TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
            ^ ast.name có LHS = NumberType(), RHS = .....
            ^ ast.condExpr có LHS = BoolType(), RHS = .....
            ^ ast.updExpr có LHS = NumberType(), RHS = .....
        """        

 
        
        
        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, [{}] + param) #! tăng tầm vực mới
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
    

    def visitReturn(self, ast, param):
        """
            TODO giống phần kiểm tra TypeCannotBeInferred (ném ra ast) và TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
            ^ chú ý : ban đầu sẽ xem xét ast.expr = none hay không để gán VoidType()
            ^ xét self.function.typ và typeReturn (type sau khi visit) giống lHS và RHs nhưng self.function.typ nhận giá trị None (suy nghĩ giống Zcode) or Type
            ^ LHS =  self.function.typ, RHS = ......
        """


    def visitAssign(self, ast, param):
        """
            TODO giống phần kiểm tra TypeCannotBeInferred và TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
        """

            

    def visitBinaryOp(self, ast, param):
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ visit left và right của BinaryOp
            ^ ['+', '-', '*', '/', '%'] -> kiểu numbertype -> return Numbertype
              ^ nếu left và right đề có type -> kiểm tra nén lỗi TypeMismatchInExpression
              ^ nếu in trong 2 left và right đề có type -> kiểm tra nén lỗi TypeMismatchInExpression và gán type left/right
              ^ nếu cả 2 left và right là kiểu Zcode -> gán type left và right
            ^ ['=', '!=', '<', '>', '>=', '<='] -> kiểu numbertype -> return Numbertype
            ^ ['and', 'or'] -> kiểu booltype -> return booltype
            ^ ['=='] -> kiểu stringtype -> return booltype
            ^ ['...'] -> kiểu stringtype -> return stringtype
            
            ^ gợi ý ['+', '-', '*', '/', '%']
                ^ b + c
                ^ xét đầu tiên là LHS_b = NumberType, RHS_b = self.visit(b)
                ^ xét đầu tiên là LHS_c = NumberType, RHS_c = self.visit(c)
                ^ return NumberType
                
        """        
        
  

    def visitUnaryOp(self, ast, param):
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ visit ast.operand của UnaryOp
            ^ '+', '-' -> kiểu numbertype -> return Numbertype
            ^ ['not'] -> kiểu booltype -> return booltype
        """       


    def visitArrayCell(self, ast, param):
        """
            TODO kiểm tra TypeMismatchInExpression
            ^ Phần type ast.arr phải là array type ->  TypeMismatchInExpression -> không thể suy diễn kiểu biết arraytype phần tham số đâu :((, nên hỏi thầy đi nha 
        """ 
     
        
        """
            TODO kiểm tra TypeMismatchInExpression
            ^ Phần ast.idx với LHS = NumberType(), RHS = .... từng phần tử trong ast.idx
        """         
   

       
        """
            TODO kiểm tra TypeMismatchInExpression kiểm tra len(left.size) và len(ast.idx) 
            ^ left là sau khi visit ast.arr: Expr 
            ^ len(left.size) < len(ast.idx) -> trả về lỗi TypeMismatchInExpression ví dụ
            number a[1,2]
            var c <- a[1,2,3]
            ^ len(left.size) = len(ast.idx) -> trả về type eleType không phải là arraytype
            number a[1,2]
            var c <- a[1,2] -> c : numbertype
            ^ len(left.size) > len(ast.idx) -> trả về arraytype cắt đi đoạn ban đầu
            number a[1,2,3]
            var c <- a[1] -> c : number c[2,3]                   
        """ 
   


            


    """phần này sẽ là cố định do ngắn quá :(( """
    def visitArrayLiteral(self, ast, param):
        #! code chỉ mang tính tham khảo, do BTL này không yêu cầu lỗi khác nhau ArrayLiteral nên thầy ko cho TypeCannotBeInferred
        for item in ast.value: self.visit(item, param)
        typ = self.visit(ast.value[0], param)
        
        #! đệ quy
        if type(typ) in [StringType, BoolType, NumberType]:
            return ArrayType([len(ast.value)], typ)
        return ArrayType([len(ast.value)] + typ.size, typ.eleType)
    
    def visitBlock(self, ast, param):
        for item in ast.stmt:
            #! trường hợp gặp block
            if type(item) is Block: self.visit(item, [{}] + param)
            else: self.visit(item, param)
            
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
