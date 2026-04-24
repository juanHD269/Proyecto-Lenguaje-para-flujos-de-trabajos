# Generated from WhileLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .WhileLangParser import WhileLangParser
else:
    from WhileLangParser import WhileLangParser

# This class defines a complete generic visitor for a parse tree produced by WhileLangParser.

class WhileLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WhileLangParser#program.
    def visitProgram(self, ctx:WhileLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#statement.
    def visitStatement(self, ctx:WhileLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#assignment.
    def visitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#whileStmt.
    def visitWhileStmt(self, ctx:WhileLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#ifStmt.
    def visitIfStmt(self, ctx:WhileLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#expression.
    def visitExpression(self, ctx:WhileLangParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:WhileLangParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:WhileLangParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#primary.
    def visitPrimary(self, ctx:WhileLangParser.PrimaryContext):
        return self.visitChildren(ctx)



del WhileLangParser