# Generated from WhileLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .WhileLangParser import WhileLangParser
else:
    from WhileLangParser import WhileLangParser

# This class defines a complete listener for a parse tree produced by WhileLangParser.
class WhileLangListener(ParseTreeListener):

    # Enter a parse tree produced by WhileLangParser#program.
    def enterProgram(self, ctx:WhileLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by WhileLangParser#program.
    def exitProgram(self, ctx:WhileLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by WhileLangParser#statement.
    def enterStatement(self, ctx:WhileLangParser.StatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#statement.
    def exitStatement(self, ctx:WhileLangParser.StatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#assignment.
    def enterAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by WhileLangParser#assignment.
    def exitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by WhileLangParser#whileStmt.
    def enterWhileStmt(self, ctx:WhileLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by WhileLangParser#whileStmt.
    def exitWhileStmt(self, ctx:WhileLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ifStmt.
    def enterIfStmt(self, ctx:WhileLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ifStmt.
    def exitIfStmt(self, ctx:WhileLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by WhileLangParser#expression.
    def enterExpression(self, ctx:WhileLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by WhileLangParser#expression.
    def exitExpression(self, ctx:WhileLangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by WhileLangParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:WhileLangParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by WhileLangParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:WhileLangParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by WhileLangParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:WhileLangParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by WhileLangParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:WhileLangParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by WhileLangParser#primary.
    def enterPrimary(self, ctx:WhileLangParser.PrimaryContext):
        pass

    # Exit a parse tree produced by WhileLangParser#primary.
    def exitPrimary(self, ctx:WhileLangParser.PrimaryContext):
        pass



del WhileLangParser