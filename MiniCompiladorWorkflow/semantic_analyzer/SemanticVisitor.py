from generated.gramaticaVisitor import gramaticaVisitor
from .SymbolTable import SymbolTable
from generated.gramaticaParser import gramaticaParser

class SemanticVisitor(gramaticaVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.defined_tasks = set()
        self.all_tasks = [] # Ordered list of task names
        self.transitions = [] # List of (from_task, to_task)
        self.current_task = None
        self.last_task_defined = None

    def visitProgram(self, ctx):
        # Pass 0: Collect all defined task names
        if ctx.children:
            for child in ctx.children:
                if isinstance(child, gramaticaParser.TaskContext):
                    task_name = child.ID().getText()
                    if task_name in self.defined_tasks:
                        raise Exception(f"Semantic Error: Task '{task_name}' is already defined.")
                    self.defined_tasks.add(task_name)
                    self.all_tasks.append(task_name)

        # Pass 1: Collect all transitions (including nested ones)
        self.visitChildren(ctx)

        # Pass 2: check for cycles (infinite loops)
        self.check_for_cycles()
        
        return None

    def check_for_cycles(self):
        adj = {task: [] for task in self.all_tasks}
        for u, v in self.transitions:
            if u in adj:
                adj[u].append(v)
        
        visited = set()
        rec_stack = set()
        
        def has_cycle(u):
            visited.add(u)
            rec_stack.add(u)
            
            for v in adj.get(u, []):
                if v not in visited:
                    if has_cycle(v):
                        return True
                elif v in rec_stack:
                    return True
            
            rec_stack.remove(u)
            return False

        for task in self.all_tasks:
            if task not in visited:
                if has_cycle(task):
                    raise Exception(f"Semantic Error: Infinite loop detected in workflow starting from task '{task}'.")

    def visitTask(self, ctx):
        task_name = ctx.ID().getText()
        self.current_task = task_name
        self.last_task_defined = task_name
        result = self.visitChildren(ctx)
        self.current_task = None
        return result

    def visitTransition(self, ctx):
        target_task = ctx.ID().getText()
        if target_task not in self.defined_tasks:
            raise Exception(f"Semantic Error: Transition to undefined task '{target_task}'.")
        
        source_task = self.current_task if self.current_task else self.last_task_defined
        if source_task:
            self.transitions.append((source_task, target_task))
            
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        self.visit(ctx.expression())
        self.symbol_table.declare(var_name, 'int')

    def visitInputStmt(self, ctx):
        var_name = ctx.ID().getText()
        self.symbol_table.declare(var_name, 'int')

    def visitPrimary(self, ctx):
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name == 'estado': # Reserved word for professor's example
                return
            if not self.symbol_table.exists(var_name):
                raise Exception(f"Semantic Error: Variable '{var_name}' not defined.")
        return self.visitChildren(ctx)
