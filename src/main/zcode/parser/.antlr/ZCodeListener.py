# Generated from c:/Users/HIEU/Desktop/BTL PPL/assignment3-initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#listDeclared.
    def enterListDeclared(self, ctx:ZCodeParser.ListDeclaredContext):
        pass

    # Exit a parse tree produced by ZCodeParser#listDeclared.
    def exitListDeclared(self, ctx:ZCodeParser.ListDeclaredContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declared.
    def enterDeclared(self, ctx:ZCodeParser.DeclaredContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declared.
    def exitDeclared(self, ctx:ZCodeParser.DeclaredContext):
        pass


    # Enter a parse tree produced by ZCodeParser#variablesDeclared.
    def enterVariablesDeclared(self, ctx:ZCodeParser.VariablesDeclaredContext):
        pass

    # Exit a parse tree produced by ZCodeParser#variablesDeclared.
    def exitVariablesDeclared(self, ctx:ZCodeParser.VariablesDeclaredContext):
        pass


    # Enter a parse tree produced by ZCodeParser#explicitTypeDeclared.
    def enterExplicitTypeDeclared(self, ctx:ZCodeParser.ExplicitTypeDeclaredContext):
        pass

    # Exit a parse tree produced by ZCodeParser#explicitTypeDeclared.
    def exitExplicitTypeDeclared(self, ctx:ZCodeParser.ExplicitTypeDeclaredContext):
        pass


    # Enter a parse tree produced by ZCodeParser#explicitType.
    def enterExplicitType(self, ctx:ZCodeParser.ExplicitTypeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#explicitType.
    def exitExplicitType(self, ctx:ZCodeParser.ExplicitTypeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#implicitVarDeclared.
    def enterImplicitVarDeclared(self, ctx:ZCodeParser.ImplicitVarDeclaredContext):
        pass

    # Exit a parse tree produced by ZCodeParser#implicitVarDeclared.
    def exitImplicitVarDeclared(self, ctx:ZCodeParser.ImplicitVarDeclaredContext):
        pass


    # Enter a parse tree produced by ZCodeParser#implicitDynamicDeclared.
    def enterImplicitDynamicDeclared(self, ctx:ZCodeParser.ImplicitDynamicDeclaredContext):
        pass

    # Exit a parse tree produced by ZCodeParser#implicitDynamicDeclared.
    def exitImplicitDynamicDeclared(self, ctx:ZCodeParser.ImplicitDynamicDeclaredContext):
        pass


    # Enter a parse tree produced by ZCodeParser#initVariableValueOrNull.
    def enterInitVariableValueOrNull(self, ctx:ZCodeParser.InitVariableValueOrNullContext):
        pass

    # Exit a parse tree produced by ZCodeParser#initVariableValueOrNull.
    def exitInitVariableValueOrNull(self, ctx:ZCodeParser.InitVariableValueOrNullContext):
        pass


    # Enter a parse tree produced by ZCodeParser#initVariableValue.
    def enterInitVariableValue(self, ctx:ZCodeParser.InitVariableValueContext):
        pass

    # Exit a parse tree produced by ZCodeParser#initVariableValue.
    def exitInitVariableValue(self, ctx:ZCodeParser.InitVariableValueContext):
        pass


    # Enter a parse tree produced by ZCodeParser#numbersList.
    def enterNumbersList(self, ctx:ZCodeParser.NumbersListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#numbersList.
    def exitNumbersList(self, ctx:ZCodeParser.NumbersListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#functionDeclared.
    def enterFunctionDeclared(self, ctx:ZCodeParser.FunctionDeclaredContext):
        pass

    # Exit a parse tree produced by ZCodeParser#functionDeclared.
    def exitFunctionDeclared(self, ctx:ZCodeParser.FunctionDeclaredContext):
        pass


    # Enter a parse tree produced by ZCodeParser#prametersList.
    def enterPrametersList(self, ctx:ZCodeParser.PrametersListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#prametersList.
    def exitPrametersList(self, ctx:ZCodeParser.PrametersListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramsPrime.
    def enterParamsPrime(self, ctx:ZCodeParser.ParamsPrimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramsPrime.
    def exitParamsPrime(self, ctx:ZCodeParser.ParamsPrimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param.
    def enterParam(self, ctx:ZCodeParser.ParamContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param.
    def exitParam(self, ctx:ZCodeParser.ParamContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statementList.
    def enterStatementList(self, ctx:ZCodeParser.StatementListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statementList.
    def exitStatementList(self, ctx:ZCodeParser.StatementListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement.
    def enterStatement(self, ctx:ZCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement.
    def exitStatement(self, ctx:ZCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declaredStatement.
    def enterDeclaredStatement(self, ctx:ZCodeParser.DeclaredStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declaredStatement.
    def exitDeclaredStatement(self, ctx:ZCodeParser.DeclaredStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:ZCodeParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:ZCodeParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#indexOperatorNew.
    def enterIndexOperatorNew(self, ctx:ZCodeParser.IndexOperatorNewContext):
        pass

    # Exit a parse tree produced by ZCodeParser#indexOperatorNew.
    def exitIndexOperatorNew(self, ctx:ZCodeParser.IndexOperatorNewContext):
        pass


    # Enter a parse tree produced by ZCodeParser#conditionStatement.
    def enterConditionStatement(self, ctx:ZCodeParser.ConditionStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#conditionStatement.
    def exitConditionStatement(self, ctx:ZCodeParser.ConditionStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elseIfStatement.
    def enterElseIfStatement(self, ctx:ZCodeParser.ElseIfStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elseIfStatement.
    def exitElseIfStatement(self, ctx:ZCodeParser.ElseIfStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elseStatement.
    def enterElseStatement(self, ctx:ZCodeParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elseStatement.
    def exitElseStatement(self, ctx:ZCodeParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#conditionAndStatement.
    def enterConditionAndStatement(self, ctx:ZCodeParser.ConditionAndStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#conditionAndStatement.
    def exitConditionAndStatement(self, ctx:ZCodeParser.ConditionAndStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#conditionExpress.
    def enterConditionExpress(self, ctx:ZCodeParser.ConditionExpressContext):
        pass

    # Exit a parse tree produced by ZCodeParser#conditionExpress.
    def exitConditionExpress(self, ctx:ZCodeParser.ConditionExpressContext):
        pass


    # Enter a parse tree produced by ZCodeParser#forStatement.
    def enterForStatement(self, ctx:ZCodeParser.ForStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#forStatement.
    def exitForStatement(self, ctx:ZCodeParser.ForStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continueStatement.
    def enterContinueStatement(self, ctx:ZCodeParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continueStatement.
    def exitContinueStatement(self, ctx:ZCodeParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#breakStatement.
    def enterBreakStatement(self, ctx:ZCodeParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#breakStatement.
    def exitBreakStatement(self, ctx:ZCodeParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#returnStatement.
    def enterReturnStatement(self, ctx:ZCodeParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#returnStatement.
    def exitReturnStatement(self, ctx:ZCodeParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#blockStatement.
    def enterBlockStatement(self, ctx:ZCodeParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#blockStatement.
    def exitBlockStatement(self, ctx:ZCodeParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#callFunction.
    def enterCallFunction(self, ctx:ZCodeParser.CallFunctionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#callFunction.
    def exitCallFunction(self, ctx:ZCodeParser.CallFunctionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#callStatement.
    def enterCallStatement(self, ctx:ZCodeParser.CallStatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#callStatement.
    def exitCallStatement(self, ctx:ZCodeParser.CallStatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expressList.
    def enterExpressList(self, ctx:ZCodeParser.ExpressListContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expressList.
    def exitExpressList(self, ctx:ZCodeParser.ExpressListContext):
        pass


    # Enter a parse tree produced by ZCodeParser#express.
    def enterExpress(self, ctx:ZCodeParser.ExpressContext):
        pass

    # Exit a parse tree produced by ZCodeParser#express.
    def exitExpress(self, ctx:ZCodeParser.ExpressContext):
        pass


    # Enter a parse tree produced by ZCodeParser#express1.
    def enterExpress1(self, ctx:ZCodeParser.Express1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#express1.
    def exitExpress1(self, ctx:ZCodeParser.Express1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#express2.
    def enterExpress2(self, ctx:ZCodeParser.Express2Context):
        pass

    # Exit a parse tree produced by ZCodeParser#express2.
    def exitExpress2(self, ctx:ZCodeParser.Express2Context):
        pass


    # Enter a parse tree produced by ZCodeParser#express3.
    def enterExpress3(self, ctx:ZCodeParser.Express3Context):
        pass

    # Exit a parse tree produced by ZCodeParser#express3.
    def exitExpress3(self, ctx:ZCodeParser.Express3Context):
        pass


    # Enter a parse tree produced by ZCodeParser#express4.
    def enterExpress4(self, ctx:ZCodeParser.Express4Context):
        pass

    # Exit a parse tree produced by ZCodeParser#express4.
    def exitExpress4(self, ctx:ZCodeParser.Express4Context):
        pass


    # Enter a parse tree produced by ZCodeParser#express5.
    def enterExpress5(self, ctx:ZCodeParser.Express5Context):
        pass

    # Exit a parse tree produced by ZCodeParser#express5.
    def exitExpress5(self, ctx:ZCodeParser.Express5Context):
        pass


    # Enter a parse tree produced by ZCodeParser#express6.
    def enterExpress6(self, ctx:ZCodeParser.Express6Context):
        pass

    # Exit a parse tree produced by ZCodeParser#express6.
    def exitExpress6(self, ctx:ZCodeParser.Express6Context):
        pass


    # Enter a parse tree produced by ZCodeParser#express7.
    def enterExpress7(self, ctx:ZCodeParser.Express7Context):
        pass

    # Exit a parse tree produced by ZCodeParser#express7.
    def exitExpress7(self, ctx:ZCodeParser.Express7Context):
        pass


    # Enter a parse tree produced by ZCodeParser#express8.
    def enterExpress8(self, ctx:ZCodeParser.Express8Context):
        pass

    # Exit a parse tree produced by ZCodeParser#express8.
    def exitExpress8(self, ctx:ZCodeParser.Express8Context):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:ZCodeParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:ZCodeParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ignore.
    def enterIgnore(self, ctx:ZCodeParser.IgnoreContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ignore.
    def exitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        pass



del ZCodeParser