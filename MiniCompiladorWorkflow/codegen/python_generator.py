from generated.gramaticaVisitor import gramaticaVisitor
from generated.gramaticaParser import gramaticaParser

class PythonGenerator(gramaticaVisitor):
    def __init__(self):
        self.code = []
        self.indent_level = 0
        self.task_code = {} # task_name -> list of code lines
        self.current_task = None
        self.all_tasks = []
        self.last_defined_task = None
        self.variables = set()

    def generate(self, ast):
        self.visit(ast)
        final_code = ["# Generated Workflow Code", "import sys", ""]
        
        if self.variables:
            final_code.append("# Global state")
            for var in sorted(self.variables):
                final_code.append(f"{var} = None")
            final_code.append("estado = 'OK'")
            final_code.append("")

        for task_name in self.all_tasks:
            lines = self.task_code.get(task_name, [])
            final_code.append(f"def {task_name}():")
            
            if self.variables:
                var_list = ", ".join(sorted(self.variables))
                final_code.append(f"    global {var_list}, estado")
            else:
                final_code.append(f"    global estado")
                
            if not lines:
                final_code.append("    pass")
            else:
                for line in lines:
                    final_code.append(f"    {line}")
            final_code.append("")
            
        if self.all_tasks:
            first_task = self.all_tasks[0]
            final_code.append(f"if __name__ == '__main__':")
            final_code.append(f"    {first_task}()")
            
        return '\n'.join(final_code)

    def add_line(self, line):
        target = self.current_task if self.current_task else self.last_defined_task
        if target:
            if target not in self.task_code:
                self.task_code[target] = []
            self.task_code[target].append("    " * self.indent_level + line)

    def visitTask(self, ctx):
        task_name = ctx.ID().getText()
        self.current_task = task_name
        self.all_tasks.append(task_name)
        self.last_defined_task = task_name
        for stmt in ctx.statement():
            self.visit(stmt)
        self.current_task = None
        return None

    def visitTransition(self, ctx):
        target_task = ctx.ID().getText()
        if ctx.T_SI():
            condition = self.visit(ctx.expression())
            self.add_line(f"if {condition}:")
            self.indent_level += 1
            self.add_line(f"{target_task}()")
            self.add_line(f"return") 
            self.indent_level -= 1
        else:
            self.add_line(f"{target_task}()")
            self.add_line(f"return")
        return None

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        self.variables.add(var_name)
        expr = self.visit(ctx.expression())
        self.add_line(f"{var_name} = {expr}")

    def visitPrintStmt(self, ctx):
        if ctx.STRING():
            content = ctx.STRING().getText()
        else:
            content = self.visit(ctx.expression())
        self.add_line(f"print({content})")

    def visitInputStmt(self, ctx):
        var_name = ctx.ID().getText()
        self.variables.add(var_name)
        self.add_line(f"{var_name} = input('Ingrese valor para {var_name}: ')")
        self.add_line(f"try: {var_name} = int({var_name})")
        self.add_line(f"except ValueError: pass")

    def visitIfStmt(self, ctx):
        expr = self.visit(ctx.expression())
        self.add_line(f"if {expr}:")
        self.indent_level += 1
        for stmt in ctx.if_block:
            self.visit(stmt)
        self.indent_level -= 1
        if ctx.T_ELSE():
            self.add_line("else:")
            self.indent_level += 1
            for stmt in ctx.else_block:
                self.visit(stmt)
            self.indent_level -= 1

    def visitWhileStmt(self, ctx):
        expr = self.visit(ctx.expression())
        self.add_line(f"while {expr}:")
        self.indent_level += 1
        for stmt in ctx.block:
            self.visit(stmt)
        self.indent_level -= 1

    def visitExpression(self, ctx):
        return self.visit(ctx.logicalOrExpression())

    def visitLogicalOrExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicalAndExpression(0))
        result = self.visit(ctx.logicalAndExpression(0))
        for i in range(1, ctx.getChildCount(), 2):
            right = self.visit(ctx.getChild(i+1))
            result = f"({result} or {right})"
        return result

    def visitLogicalAndExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.equalityExpression(0))
        result = self.visit(ctx.equalityExpression(0))
        for i in range(1, ctx.getChildCount(), 2):
            right = self.visit(ctx.getChild(i+1))
            result = f"({result} and {right})"
        return result

    def visitEqualityExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relationalExpression(0))
        left = self.visit(ctx.relationalExpression(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.relationalExpression(1))
        return f"({left} {op} {right})"

    def visitRelationalExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.additiveExpression(0))
        left = self.visit(ctx.additiveExpression(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.additiveExpression(1))
        return f"({left} {op} {right})"

    def visitAdditiveExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiplicativeExpression(0))
        result = self.visit(ctx.multiplicativeExpression(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i+1))
            result = f"({result} {op} {right})"
        return result

    def visitMultiplicativeExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary(0))
        result = self.visit(ctx.primary(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i+1))
            result = f"({result} {op} {right})"
        return result

    def visitPrimary(self, ctx):
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name != 'estado':
                self.variables.add(var_name)
            return var_name
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.T_LPAREN():
            return f"({self.visit(ctx.expression())})"
        elif ctx.T_NOT():
            return f"(not {self.visit(ctx.primary())})"
        return ""
