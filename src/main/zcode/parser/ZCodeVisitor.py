# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#listDeclared.
    def visitListDeclared(self, ctx:ZCodeParser.ListDeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declared.
    def visitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variablesDeclared.
    def visitVariablesDeclared(self, ctx:ZCodeParser.VariablesDeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#explicitTypeDeclared.
    def visitExplicitTypeDeclared(self, ctx:ZCodeParser.ExplicitTypeDeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#explicitType.
    def visitExplicitType(self, ctx:ZCodeParser.ExplicitTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicitVarDeclared.
    def visitImplicitVarDeclared(self, ctx:ZCodeParser.ImplicitVarDeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicitDynamicDeclared.
    def visitImplicitDynamicDeclared(self, ctx:ZCodeParser.ImplicitDynamicDeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#initVariableValueOrNull.
    def visitInitVariableValueOrNull(self, ctx:ZCodeParser.InitVariableValueOrNullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#initVariableValue.
    def visitInitVariableValue(self, ctx:ZCodeParser.InitVariableValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numbersList.
    def visitNumbersList(self, ctx:ZCodeParser.NumbersListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#functionDeclared.
    def visitFunctionDeclared(self, ctx:ZCodeParser.FunctionDeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#prametersList.
    def visitPrametersList(self, ctx:ZCodeParser.PrametersListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramsPrime.
    def visitParamsPrime(self, ctx:ZCodeParser.ParamsPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statementList.
    def visitStatementList(self, ctx:ZCodeParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaredStatement.
    def visitDeclaredStatement(self, ctx:ZCodeParser.DeclaredStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:ZCodeParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexOperatorNew.
    def visitIndexOperatorNew(self, ctx:ZCodeParser.IndexOperatorNewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#conditionStatement.
    def visitConditionStatement(self, ctx:ZCodeParser.ConditionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elseIfStatement.
    def visitElseIfStatement(self, ctx:ZCodeParser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elseStatement.
    def visitElseStatement(self, ctx:ZCodeParser.ElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#conditionAndStatement.
    def visitConditionAndStatement(self, ctx:ZCodeParser.ConditionAndStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#conditionExpress.
    def visitConditionExpress(self, ctx:ZCodeParser.ConditionExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forStatement.
    def visitForStatement(self, ctx:ZCodeParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continueStatement.
    def visitContinueStatement(self, ctx:ZCodeParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakStatement.
    def visitBreakStatement(self, ctx:ZCodeParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnStatement.
    def visitReturnStatement(self, ctx:ZCodeParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockStatement.
    def visitBlockStatement(self, ctx:ZCodeParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#callFunction.
    def visitCallFunction(self, ctx:ZCodeParser.CallFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#callStatement.
    def visitCallStatement(self, ctx:ZCodeParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expressList.
    def visitExpressList(self, ctx:ZCodeParser.ExpressListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#express.
    def visitExpress(self, ctx:ZCodeParser.ExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#express1.
    def visitExpress1(self, ctx:ZCodeParser.Express1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#express2.
    def visitExpress2(self, ctx:ZCodeParser.Express2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#express3.
    def visitExpress3(self, ctx:ZCodeParser.Express3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#express4.
    def visitExpress4(self, ctx:ZCodeParser.Express4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#express5.
    def visitExpress5(self, ctx:ZCodeParser.Express5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#express6.
    def visitExpress6(self, ctx:ZCodeParser.Express6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#express7.
    def visitExpress7(self, ctx:ZCodeParser.Express7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#express8.
    def visitExpress8(self, ctx:ZCodeParser.Express8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:ZCodeParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore.
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return self.visitChildren(ctx)



del ZCodeParser