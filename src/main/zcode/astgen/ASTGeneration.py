from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    # # Visit a parse tree produced by ZCodeParser#program.
    # program: NEWLINE* listDeclared EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        
        return Program(self.visit(ctx.listDeclared()))

    # Visit a parse tree produced by ZCodeParser#listDeclared.
    # listDeclared: declared listDeclared | declared;
    def visitListDeclared(self, ctx:ZCodeParser.ListDeclaredContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.declared())]

        return  [self.visit(ctx.declared())] + self.visit(ctx.listDeclared())

    # Visit a parse tree produced by ZCodeParser#declared.
    # declared: functionDeclared | variablesDeclared ignore;
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ZCodeParser#variablesDeclared.
    # variablesDeclared: explicitTypeDeclared | implicitVarDeclared  | implicitDynamicDeclared;
    def visitVariablesDeclared(self, ctx:ZCodeParser.VariablesDeclaredContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by ZCodeParser#explicitTypeDeclared.
    # explicitTypeDeclared:  explicitType ID initVariableValueOrNull | explicitType ID LBRACK numbersList RBRACK initVariableValueOrNull;
    def visitExplicitTypeDeclared(self, ctx:ZCodeParser.ExplicitTypeDeclaredContext):
        type = self.visit(ctx.explicitType())
        if ctx.numbersList():
            type =  ArrayType(self.visit(ctx.numbersList()) , self.visit(ctx.explicitType()))
                
        return VarDecl(Id(ctx.ID().getText()), type , None, self.visit(ctx.initVariableValueOrNull()))
        
        
    # Visit a parse tree produced by ZCodeParser#explicitType.
    # explicitType: STRING | BOOL | NUMBER;
    def visitExplicitType(self, ctx:ZCodeParser.ExplicitTypeContext):
        if ctx.STRING():
            return StringType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.NUMBER():
            return NumberType()
        return None

    # Visit a parse tree produced by ZCodeParser#implicitVarDeclared.
    # implicitVarDeclared: VAR ID initVariableValue;
    def visitImplicitVarDeclared(self, ctx:ZCodeParser.ImplicitVarDeclaredContext):
        return  VarDecl(Id(ctx.ID().getText()), None , ctx.VAR().getText() , self.visit(ctx.initVariableValue()))


    # Visit a parse tree produced by ZCodeParser#implicitDynamicDeclared.
    # implicitDynamicDeclared: DYNAMIC ID initVariableValueOrNull;
    def visitImplicitDynamicDeclared(self, ctx:ZCodeParser.ImplicitDynamicDeclaredContext):
        return  VarDecl(Id(ctx.ID().getText()), None , ctx.DYNAMIC().getText() , self.visit(ctx.initVariableValueOrNull()))


    # Visit a parse tree produced by ZCodeParser#initVariableValueOrNull.
    # initVariableValueOrNull: ASSIGN express | ;
    def visitInitVariableValueOrNull(self, ctx:ZCodeParser.InitVariableValueOrNullContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.express())

        return None

    # Visit a parse tree produced by ZCodeParser#initVariableValue.
    # initVariableValue: ASSIGN express;
    def visitInitVariableValue(self, ctx:ZCodeParser.InitVariableValueContext):
        return self.visit(ctx.express())


    # Visit a parse tree produced by ZCodeParser#numbersList.
    # numbersList: NUMBERLIT COMMA numbersList | NUMBERLIT;
    def visitNumbersList(self, ctx:ZCodeParser.NumbersListContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUMBERLIT().getText())]
    
        return [float(ctx.NUMBERLIT().getText())] + self.visit(ctx.numbersList())


    # Visit a parse tree produced by ZCodeParser#functionDeclared.
    # functionDeclared: FUNC ID LPAREN prametersList RPAREN (ignore? blockStatement | ignore? returnStatement | ignore);
    def visitFunctionDeclared(self, ctx:ZCodeParser.FunctionDeclaredContext):
        pramList = self.visit(ctx.prametersList())
        
        if ctx.blockStatement():
            return FuncDecl(Id(ctx.ID().getText()) , pramList , self.visit(ctx.blockStatement()))
        elif ctx.returnStatement():
            return FuncDecl(Id(ctx.ID().getText()) , pramList , self.visit(ctx.returnStatement()))
        
        return  FuncDecl(Id(ctx.ID().getText()) , pramList , None)
            

    # Visit a parse tree produced by ZCodeParser#prametersList.
    # prametersList: paramsPrime | ;
    def visitPrametersList(self, ctx:ZCodeParser.PrametersListContext):
        if ctx.getChildCount() == 0:
            return []
        
        return self.visit(ctx.paramsPrime())


    # Visit a parse tree produced by ZCodeParser#paramsPrime.
    # paramsPrime: param COMMA paramsPrime | param;
    def visitParamsPrime(self, ctx:ZCodeParser.ParamsPrimeContext):
        if ctx.paramsPrime():
            return [self.visit(ctx.param())] + self.visit(ctx.paramsPrime())

        return [self.visit(ctx.param())]


    # Visit a parse tree produced by ZCodeParser#param.
    # param: explicitType (ID | ID LBRACK numbersList RBRACK);
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        if ctx.getChildCount() == 2: 
            return VarDecl(Id(ctx.ID().getText()) , self.visit(ctx.explicitType()) )
    
        return VarDecl(Id(ctx.ID().getText()) , ArrayType(self.visit(ctx.numbersList()) , self.visit(ctx.explicitType())))

    
    # Visit a parse tree produced by ZCodeParser#statementList.
    # statementList: statement statementList | ;
    def visitStatementList(self, ctx:ZCodeParser.StatementListContext):
        if ctx.getChildCount() == 0:
            return []
        
        return  [self.visit(ctx.statement())] + self.visit(ctx.statementList())

    
    # Visit a parse tree produced by ZCodeParser#statement.
    # statement: declaredStatement | assignmentStatement | conditionStatement | forStatement 
    #            | breakStatement | continueStatement | returnStatement | callStatement | blockStatement;
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visit(ctx.getChild(0))

    
    # Visit a parse tree produced by ZCodeParser#declaredStatement.
    # declaredStatement: variablesDeclared ignore;
    def visitDeclaredStatement(self, ctx:ZCodeParser.DeclaredStatementContext):
        return self.visit(ctx.variablesDeclared())

    
    # Visit a parse tree produced by ZCodeParser#assignmentStatement.
    # assignmentStatement: (ID | ID indexOperatorNew) ASSIGN express ignore;
    def visitAssignmentStatement(self, ctx:ZCodeParser.AssignmentStatementContext):
        if ctx.indexOperatorNew():
            return Assign(ArrayCell(Id(ctx.ID().getText()) , self.visit(ctx.indexOperatorNew()))  , self.visit(ctx.express()))
        
        return Assign(Id(ctx.ID().getText()) , self.visit(ctx.express()))
        
    
    # Visit a parse tree produced by ZCodeParser#indexOperatorNew.
    # indexOperatorNew: (LBRACK expressList RBRACK);
    def visitIndexOperatorNew(self, ctx:ZCodeParser.IndexOperatorNewContext):
        return self.visit(ctx.expressList())

    
    # Visit a parse tree produced by ZCodeParser#conditionStatement.
    # conditionStatement: IF conditionAndStatement (elseIfStatement | ) (elseStatement | );
    def visitConditionStatement(self, ctx:ZCodeParser.ConditionStatementContext):
        (condition_exp , statement) = self.visit(ctx.conditionAndStatement())
        elifStmt = self.visit(ctx.elseIfStatement()) if ctx.elseIfStatement() else []
        elseStmt = self.visit(ctx.elseStatement()) if ctx.elseStatement() else None

        return If(condition_exp, statement , elifStmt , elseStmt)

    
    # Visit a parse tree produced by ZCodeParser#elseIfStatement.
    # elseIfStatement: ELIF conditionAndStatement elseIfStatement | ELIF conditionAndStatement;
    def visitElseIfStatement(self, ctx:ZCodeParser.ElseIfStatementContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.conditionAndStatement())]
        
        return [self.visit(ctx.conditionAndStatement())] + self.visit(ctx.elseIfStatement())

    
    # Visit a parse tree produced by ZCodeParser#elseStatement.
    # elseStatement: ELSE ignore statement | ELSE statement;
    def visitElseStatement(self, ctx:ZCodeParser.ElseStatementContext):
        return self.visit(ctx.statement())  

    
    # Visit a parse tree produced by ZCodeParser#conditionAndStatement.
    # conditionAndStatement: conditionExpress (ignore statement | statement);
    def visitConditionAndStatement(self, ctx:ZCodeParser.ConditionAndStatementContext):
        return (self.visit(ctx.conditionExpress()), self.visit(ctx.statement()))

    
    # Visit a parse tree produced by ZCodeParser#conditionExpress.
    # conditionExpress: LPAREN express RPAREN;
    def visitConditionExpress(self, ctx:ZCodeParser.ConditionExpressContext):
        return self.visit(ctx.express())

    
    # Visit a parse tree produced by ZCodeParser#forStatement.
    # forStatement: FOR ID UNTIL express BY express (statement | ignore statement);
    def visitForStatement(self, ctx:ZCodeParser.ForStatementContext):
        loop_variable = Id(ctx.ID().getText())
        condition_expr = self.visit(ctx.express(0))
        update_expr = self.visit(ctx.express(1))
        loop_body = self.visit(ctx.statement())   

        return For(loop_variable, condition_expr, update_expr, loop_body)

    
    # Visit a parse tree produced by ZCodeParser#continueStatement.
    # continueStatement: CONTINUE ignore;
    def visitContinueStatement(self, ctx:ZCodeParser.ContinueStatementContext):
        return Continue()

    
    # Visit a parse tree produced by ZCodeParser#breakStatement.
    # breakStatement: BREAK ignore;
    def visitBreakStatement(self, ctx:ZCodeParser.BreakStatementContext):
        return Break()

    
    # Visit a parse tree produced by ZCodeParser#returnStatement.
    # returnStatement: RETURN (express | ) ignore; 
    def visitReturnStatement(self, ctx:ZCodeParser.ReturnStatementContext):
        if ctx.express():
            return Return(self.visit(ctx.express()))
        
        return Return()

    
    # Visit a parse tree produced by ZCodeParser#blockStatement.
    # blockStatement:  BEGIN ignore (statementList | ) END ignore;
    def visitBlockStatement(self, ctx:ZCodeParser.BlockStatementContext):
        statements = self.visit(ctx.statementList()) if ctx.statementList() else []
        
        return Block(statements)

    
    # Visit a parse tree produced by ZCodeParser#callFunction.
    # callFunction: ID LPAREN (expressList | ) RPAREN;
    def visitCallFunction(self, ctx:ZCodeParser.CallFunctionContext):
        function_name = ctx.ID().getText()
        arguments = self.visit(ctx.expressList()) if ctx.expressList() else []
        
        return CallExpr(Id(function_name), arguments)

    
    # Visit a parse tree produced by ZCodeParser#callStatement.
    # callStatement: ID LPAREN (expressList | ) RPAREN ignore;
    def visitCallStatement(self, ctx:ZCodeParser.CallStatementContext):
        function_name = ctx.ID().getText()
        arguments = self.visit(ctx.expressList()) if ctx.expressList() else []
        
        return CallStmt(Id(function_name), arguments)

    
    # Visit a parse tree produced by ZCodeParser#expressList.
    # expressList: express COMMA expressList | express;
    def visitExpressList(self, ctx:ZCodeParser.ExpressListContext):
        if ctx.getChildCount() == 1:
             return [self.visit(ctx.express())]
        
        return [self.visit(ctx.express())] + self.visit(ctx.expressList())

    
    # Visit a parse tree produced by ZCodeParser#express.
    # express:  express1 CONCAT express1 | express1;
    def visitExpress(self, ctx:ZCodeParser.ExpressContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express1(0))
        
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.express1(0))
        right = self.visit(ctx.express1(1))

        return BinaryOp(op, left, right)

    
    # Visit a parse tree produced by ZCodeParser#express1.
    # express1: express2 (EQ | EQEQ | NEQ | LT | GT | LTE | GTE ) express2 | express2;
    def visitExpress1(self, ctx:ZCodeParser.Express1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express2(0))
        
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.express2(0))
        right = self.visit(ctx.express2(1))

        return BinaryOp(op, left, right)

    
    # Visit a parse tree produced by ZCodeParser#express2.
    # express2: express2 (AND | OR) express3 | express3;
    def visitExpress2(self, ctx:ZCodeParser.Express2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express3())
        
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.express2())
        right = self.visit(ctx.express3())

        return BinaryOp(op, left, right)

    
    # Visit a parse tree produced by ZCodeParser#express3.
    # express3: express3 (ADD | SUB) express4 | express4;
    def visitExpress3(self, ctx:ZCodeParser.Express3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express4())
        
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.express3())
        right = self.visit(ctx.express4())

        return BinaryOp(op, left, right)

    
    # Visit a parse tree produced by ZCodeParser#express4.
    # express4: express4 (MUL | DIV | MOD) express5 | express5;
    def visitExpress4(self, ctx:ZCodeParser.Express4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express5())
        
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.express4())
        right = self.visit(ctx.express5())

        return BinaryOp(op, left, right)

    
    # Visit a parse tree produced by ZCodeParser#express5.
    # express5: NOT express5 | express6;
    def visitExpress5(self, ctx:ZCodeParser.Express5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.NOT().getText() , self.visit(ctx.express5()))
        
        return self.visit(ctx.express6())
         
    
    # Visit a parse tree produced by ZCodeParser#express6.
    # express6: SUB express6 | express7 | express8;
    def visitExpress6(self, ctx:ZCodeParser.Express6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.SUB().getText() , self.visit(ctx.express6()))
        elif ctx.express7():
            return self.visit(ctx.express7())
        
        return self.visit(ctx.express8())

    
    # Visit a parse tree produced by ZCodeParser#express7.
    # express7: (ID | callFunction) (LBRACK expressList RBRACK);  
    def visitExpress7(self, ctx:ZCodeParser.Express7Context):
        if ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()) , self.visit(ctx.expressList()))
        
        return ArrayCell(self.visit(ctx.callFunction()) , self.visit(ctx.expressList()))

    
    # Visit a parse tree produced by ZCodeParser#express8.
    # express8: NUMBERLIT | STRINGLIT | TRUE | FALSE | ID | arrayLiteral | (LPAREN express RPAREN) | callFunction;
    def visitExpress8(self, ctx:ZCodeParser.Express8Context):
        if ctx.NUMBERLIT():
            return NumberLiteral(float(ctx.NUMBERLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.arrayLiteral():
            return self.visit(ctx.arrayLiteral())
        elif ctx.callFunction():
            return self.visit(ctx.callFunction())
        
        return self.visit(ctx.express())

    
    # Visit a parse tree produced by ZCodeParser#arrayLiteral.
    # arrayLiteral: LBRACK expressList RBRACK; 
    def visitArrayLiteral(self, ctx:ZCodeParser.ArrayLiteralContext):
        return ArrayLiteral(self.visit(ctx.expressList()))

    
    # Visit a parse tree produced by ZCodeParser#ignore. 
    # ignore: NEWLINE+;
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return None