from generated.WhileLangVisitor import WhileLangVisitor
from .symbol_table import SymbolTable

class SemanticVisitor(WhileLangVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        # Assume all variables are int for simplicity
        self.symbol_table.declare(var_name, 'int')
        return self.visitChildren(ctx)

    def visitExpression(self, ctx):
        # Basic type checking, assume int
        return 'int'