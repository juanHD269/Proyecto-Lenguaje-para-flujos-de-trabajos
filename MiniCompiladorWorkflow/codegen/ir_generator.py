from generated.gramaticaVisitor import gramaticaVisitor
from generated.gramaticaParser import gramaticaParser

class IRGenerator(gramaticaVisitor):
    def __init__(self):
        self.instructions = []
        self.temp_count = 0
        self.label_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def generate(self, ast):
        self.visit(ast)
        return "\n".join(self.instructions)

    def visitTask(self, ctx):
        task_name = ctx.ID().getText()
        self.instructions.append(f"LABEL {task_name}:")
        return self.visitChildren(ctx)

    def visitTransition(self, ctx):
        target = ctx.ID().getText()
        if ctx.T_SI():
            cond = self.visit(ctx.expression())
            self.instructions.append(f"IF {cond} GOTO {target}")
        else:
            self.instructions.append(f"GOTO {target}")
        return None

    def visitAssignment(self, ctx):
        var = ctx.ID().getText()
        val = self.visit(ctx.expression())
        self.instructions.append(f"{var} = {val}")
        return var

    def visitExpression(self, ctx):
        return self.visit(ctx.logicalOrExpression())

    def visitLogicalOrExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicalAndExpression(0))
        result = self.visit(ctx.logicalAndExpression(0))
        for i in range(1, ctx.getChildCount(), 2):
            right = self.visit(ctx.getChild(i+1))
            temp = self.new_temp()
            self.instructions.append(f"{temp} = {result} OR {right}")
            result = temp
        return result

    def visitLogicalAndExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.equalityExpression(0))
        result = self.visit(ctx.equalityExpression(0))
        for i in range(1, ctx.getChildCount(), 2):
            right = self.visit(ctx.getChild(i+1))
            temp = self.new_temp()
            self.instructions.append(f"{temp} = {result} AND {right}")
            result = temp
        return result

    def visitEqualityExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relationalExpression(0))
        left = self.visit(ctx.relationalExpression(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.relationalExpression(1))
        temp = self.new_temp()
        self.instructions.append(f"{temp} = {left} {op} {right}")
        return temp

    def visitRelationalExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.additiveExpression(0))
        left = self.visit(ctx.additiveExpression(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.additiveExpression(1))
        temp = self.new_temp()
        self.instructions.append(f"{temp} = {left} {op} {right}")
        return temp

    def visitAdditiveExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiplicativeExpression(0))
        result = self.visit(ctx.multiplicativeExpression(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i+1))
            temp = self.new_temp()
            self.instructions.append(f"{temp} = {result} {op} {right}")
            result = temp
        return result

    def visitMultiplicativeExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary(0))
        result = self.visit(ctx.primary(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i+1))
            temp = self.new_temp()
            self.instructions.append(f"{temp} = {result} {op} {right}")
            result = temp
        return result

    def visitPrimary(self, ctx):
        if ctx.ID():
            return ctx.ID().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.T_LPAREN():
            return self.visit(ctx.expression())
        elif ctx.T_NOT():
            val = self.visit(ctx.primary())
            temp = self.new_temp()
            self.instructions.append(f"{temp} = NOT {val}")
            return temp
        return ""

    def visitInputStmt(self, ctx):
        var = ctx.ID().getText()
        self.instructions.append(f"READ {var}")
        return None

    def visitPrintStmt(self, ctx):
        if ctx.STRING():
            val = ctx.STRING().getText()
        else:
            val = self.visit(ctx.expression())
        self.instructions.append(f"PRINT {val}")
        return None

    def visitIfStmt(self, ctx):
        cond = self.visit(ctx.expression())
        else_label = self.new_label()
        end_label = self.new_label()
        self.instructions.append(f"IF NOT {cond} GOTO {else_label}")
        for stmt in ctx.if_block:
            self.visit(stmt)
        self.instructions.append(f"GOTO {end_label}")
        self.instructions.append(f"LABEL {else_label}:")
        if ctx.T_ELSE():
            for stmt in ctx.else_block:
                self.visit(stmt)
        self.instructions.append(f"LABEL {end_label}:")
        return None

    def visitWhileStmt(self, ctx):
        start_label = self.new_label()
        end_label = self.new_label()
        self.instructions.append(f"LABEL {start_label}:")
        cond = self.visit(ctx.expression())
        self.instructions.append(f"IF NOT {cond} GOTO {end_label}")
        for stmt in ctx.block:
            self.visit(stmt)
        self.instructions.append(f"GOTO {start_label}")
        self.instructions.append(f"LABEL {end_label}:")
        return None
