from generated.gramaticaVisitor import gramaticaVisitor
from generated.gramaticaParser import gramaticaParser

class PythonGenerator(gramaticaVisitor):
    """
    Clase encargada de la traducción final del AST a código Python ejecutable.
    Implementa el patrón Visitor para generar funciones y estructuras de control.
    """
    def __init__(self):
        self.code = []
        self.indent_level = 0
        self.task_code = {} # Diccionario para almacenar líneas de código por cada tarea
        self.current_task = None
        self.all_tasks = [] # Mantiene el orden de definición de las tareas
        self.last_defined_task = None
        self.variables = set() # Registro de variables para declaración global

    def generate(self, ast):
        """
        Método principal que orquesta la generación del script final.
        """
        self.visit(ast)
        final_code = ["# Generated Workflow Code", "import sys", ""]
        
        # Inicialización del estado global para persistencia entre tareas
        if self.variables:
            final_code.append("# Global state")
            for var in sorted(self.variables):
                final_code.append(f"{var} = None")
            final_code.append("estado = 'OK'") # Variable por defecto del ejemplo del profesor
            final_code.append("")

        # Generar cada tarea como una función de Python
        for task_name in self.all_tasks:
            lines = self.task_code.get(task_name, [])
            final_code.append(f"def {task_name}():")
            
            # Decisión clave: Declarar todas las variables como globales dentro de la función
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
            
        # Punto de entrada del programa (llama a la primera tarea definida)
        if self.all_tasks:
            first_task = self.all_tasks[0]
            final_code.append(f"if __name__ == '__main__':")
            final_code.append(f"    {first_task}()")
            
        return '\n'.join(final_code)

    def add_line(self, line):
        """Agrega una línea de código indentada a la tarea actual."""
        target = self.current_task if self.current_task else self.last_defined_task
        if target:
            if target not in self.task_code:
                self.task_code[target] = []
            self.task_code[target].append("    " * self.indent_level + line)

    def visitTask(self, ctx):
        """Traduce una regla 'task' a una estructura que se convertirá en función."""
        task_name = ctx.ID().getText()
        self.current_task = task_name
        self.all_tasks.append(task_name)
        self.last_defined_task = task_name
        for stmt in ctx.statement():
            self.visit(stmt)
        self.current_task = None
        return None

    def visitTransition(self, ctx):
        """Traduce 'ir_a' a una llamada de función condicional o incondicional."""
        target_task = ctx.ID().getText()
        if ctx.T_SI():
            condition = self.visit(ctx.expression())
            self.add_line(f"if {condition}:")
            self.indent_level += 1
            self.add_line(f"{target_task}()")
            self.add_line(f"return") # Asegura que no continúe la ejecución de la tarea actual
            self.indent_level -= 1
        else:
            self.add_line(f"{target_task}()")
            self.add_line(f"return")
        return None

    def visitAssignment(self, ctx):
        """Traduce asignaciones de variables."""
        var_name = ctx.ID().getText()
        self.variables.add(var_name)
        expr = self.visit(ctx.expression())
        self.add_line(f"{var_name} = {expr}")

    def visitPrintStmt(self, ctx):
        """Traduce la instrucción 'print'."""
        if ctx.STRING():
            content = ctx.STRING().getText()
        else:
            content = self.visit(ctx.expression())
        self.add_line(f"print({content})")

    def visitInputStmt(self, ctx):
        """Traduce 'input' a una entrada interactiva con manejo de tipos básicos."""
        var_name = ctx.ID().getText()
        self.variables.add(var_name)
        self.add_line(f"{var_name} = input('Ingrese valor para {var_name}: ')")
        self.add_line(f"try: {var_name} = int({var_name})") # Intento de conversión a entero
        self.add_line(f"except ValueError: pass")

    def visitIfStmt(self, ctx):
        """Traduce la estructura de control 'if'."""
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
        """Traduce el bucle 'while'."""
        expr = self.visit(ctx.expression())
        self.add_line(f"while {expr}:")
        self.indent_level += 1
        for stmt in ctx.block:
            self.visit(stmt)
        self.indent_level -= 1

    # Los métodos de visita de expresiones (visitExpression, etc.)
    # simplemente traducen los operadores de la gramática a sus equivalentes en Python.
    
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
        """Traduce los elementos base de una expresión (ID, Números, Paréntesis)."""
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
