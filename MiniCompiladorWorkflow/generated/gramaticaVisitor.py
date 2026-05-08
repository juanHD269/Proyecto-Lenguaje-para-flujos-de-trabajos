# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#program.
    def visitProgram(self, ctx:gramaticaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#task.
    def visitTask(self, ctx:gramaticaParser.TaskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#transition.
    def visitTransition(self, ctx:gramaticaParser.TransitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#statement.
    def visitStatement(self, ctx:gramaticaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#assignment.
    def visitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#printStmt.
    def visitPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#inputStmt.
    def visitInputStmt(self, ctx:gramaticaParser.InputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ifStmt.
    def visitIfStmt(self, ctx:gramaticaParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#whileStmt.
    def visitWhileStmt(self, ctx:gramaticaParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#expression.
    def visitExpression(self, ctx:gramaticaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:gramaticaParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:gramaticaParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#equalityExpression.
    def visitEqualityExpression(self, ctx:gramaticaParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#relationalExpression.
    def visitRelationalExpression(self, ctx:gramaticaParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:gramaticaParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:gramaticaParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#primary.
    def visitPrimary(self, ctx:gramaticaParser.PrimaryContext):
        return self.visitChildren(ctx)



del gramaticaParser