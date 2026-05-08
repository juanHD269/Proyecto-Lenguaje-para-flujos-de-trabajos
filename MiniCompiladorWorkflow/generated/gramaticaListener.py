# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#program.
    def enterProgram(self, ctx:gramaticaParser.ProgramContext):
        pass

    # Exit a parse tree produced by gramaticaParser#program.
    def exitProgram(self, ctx:gramaticaParser.ProgramContext):
        pass


    # Enter a parse tree produced by gramaticaParser#task.
    def enterTask(self, ctx:gramaticaParser.TaskContext):
        pass

    # Exit a parse tree produced by gramaticaParser#task.
    def exitTask(self, ctx:gramaticaParser.TaskContext):
        pass


    # Enter a parse tree produced by gramaticaParser#transition.
    def enterTransition(self, ctx:gramaticaParser.TransitionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#transition.
    def exitTransition(self, ctx:gramaticaParser.TransitionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#statement.
    def enterStatement(self, ctx:gramaticaParser.StatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#statement.
    def exitStatement(self, ctx:gramaticaParser.StatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#assignment.
    def enterAssignment(self, ctx:gramaticaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by gramaticaParser#assignment.
    def exitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by gramaticaParser#printStmt.
    def enterPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#printStmt.
    def exitPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#inputStmt.
    def enterInputStmt(self, ctx:gramaticaParser.InputStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#inputStmt.
    def exitInputStmt(self, ctx:gramaticaParser.InputStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ifStmt.
    def enterIfStmt(self, ctx:gramaticaParser.IfStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ifStmt.
    def exitIfStmt(self, ctx:gramaticaParser.IfStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#whileStmt.
    def enterWhileStmt(self, ctx:gramaticaParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#whileStmt.
    def exitWhileStmt(self, ctx:gramaticaParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#expression.
    def enterExpression(self, ctx:gramaticaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expression.
    def exitExpression(self, ctx:gramaticaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:gramaticaParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:gramaticaParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:gramaticaParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:gramaticaParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#equalityExpression.
    def enterEqualityExpression(self, ctx:gramaticaParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#equalityExpression.
    def exitEqualityExpression(self, ctx:gramaticaParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#relationalExpression.
    def enterRelationalExpression(self, ctx:gramaticaParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#relationalExpression.
    def exitRelationalExpression(self, ctx:gramaticaParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:gramaticaParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:gramaticaParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:gramaticaParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:gramaticaParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#primary.
    def enterPrimary(self, ctx:gramaticaParser.PrimaryContext):
        pass

    # Exit a parse tree produced by gramaticaParser#primary.
    def exitPrimary(self, ctx:gramaticaParser.PrimaryContext):
        pass



del gramaticaParser