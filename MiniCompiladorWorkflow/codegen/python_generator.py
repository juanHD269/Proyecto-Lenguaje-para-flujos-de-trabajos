from generated.WhileLangVisitor import WhileLangVisitor

class PythonGenerator(WhileLangVisitor):
    def __init__(self):
        self.code = []

    def generate(self, ast):
        self.visit(ast)
        return '\n'.join(self.code)

    def visitAssignment(self, ctx):
        var = ctx.ID().getText()
        expr = self.visitExpression(ctx.expression())
        self.code.append(f"{var} = {expr}")

    def visitWhileStmt(self, ctx):
        cond = self.visitExpression(ctx.expression())
        body = []
        for stmt in ctx.statement():
            # Need to collect body code
            # For simplicity, assume single statements
            pass
        # Placeholder
        self.code.append(f"while {cond}:")
        self.code.append("    pass")  # Need proper body

    def visitExpression(self, ctx):
        if ctx.primary():
            return self.visitPrimary(ctx.primary())
        elif ctx.additiveExpression():
            left = self.visitAdditiveExpression(ctx.additiveExpression(0))
            if ctx.getChildCount() > 1:
                op = ctx.getChild(1).getText()
                right = self.visitAdditiveExpression(ctx.additiveExpression(1))
                return f"({left} {op} {right})"
            return left
        return self.visitChildren(ctx)

    def visitAdditiveExpression(self, ctx):
        if ctx.multiplicativeExpression():
            left = self.visitMultiplicativeExpression(ctx.multiplicativeExpression(0))
            if ctx.getChildCount() > 1:
                op = ctx.getChild(1).getText()
                right = self.visitMultiplicativeExpression(ctx.multiplicativeExpression(1))
                return f"({left} {op} {right})"
            return left
        return self.visitChildren(ctx)

    def visitMultiplicativeExpression(self, ctx):
        if ctx.primary():
            left = self.visitPrimary(ctx.primary(0))
            if ctx.getChildCount() > 1:
                op = ctx.getChild(1).getText()
                right = self.visitPrimary(ctx.primary(1))
                return f"({left} {op} {right})"
            return left
        return self.visitChildren(ctx)

    def visitPrimary(self, ctx):
        if ctx.ID():
            return ctx.ID().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.expression():
            return f"({self.visitExpression(ctx.expression())})"
        return self.visitChildren(ctx)