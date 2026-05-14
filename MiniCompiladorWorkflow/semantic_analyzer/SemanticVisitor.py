from generated.gramaticaVisitor import gramaticaVisitor
from .SymbolTable import SymbolTable
from generated.gramaticaParser import gramaticaParser

class SemanticVisitor(gramaticaVisitor):
    """
    Clase encargada del análisis semántico del lenguaje.
    Valida que el programa tenga sentido lógico: tareas definidas, variables declaradas
    y ausencia de bucles infinitos.
    """
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.defined_tasks = set()  # Almacena nombres de tareas definidas
        self.all_tasks = []         # Lista ordenada de nombres de tareas
        self.transitions = []       # Almacena tuplas (origen, destino) para detectar ciclos
        self.current_task = None    # Tarea que se está visitando actualmente
        self.last_task_defined = None

    def visitProgram(self, ctx):
        """
        Punto de entrada del análisis semántico. Realiza varias pasadas para validar el flujo.
        """
        # PASADA 0: Recolectar todos los nombres de tareas definidas antes de validar transiciones
        if ctx.children:
            for child in ctx.children:
                if isinstance(child, gramaticaParser.TaskContext):
                    task_name = child.ID().getText()
                    if task_name in self.defined_tasks:
                        raise Exception(f"Semantic Error: Task '{task_name}' is already defined.")
                    self.defined_tasks.add(task_name)
                    self.all_tasks.append(task_name)

        # PASADA 1: Visitar hijos para recolectar transiciones y validar variables
        self.visitChildren(ctx)

        # PASADA 2: Verificar si hay ciclos (bucles infinitos) mediante grafos
        self.check_for_cycles()
        
        return None

    def check_for_cycles(self):
        """
        Implementa un algoritmo de búsqueda en profundidad (DFS) para detectar ciclos en el flujo.
        Esto cumple con el requisito del profesor de 'Detectar bucles infinitos'.
        """
        # Construir lista de adyacencia
        adj = {task: [] for task in self.all_tasks}
        for u, v in self.transitions:
            if u in adj:
                adj[u].append(v)
        
        visited = set()     # Nodos totalmente procesados
        rec_stack = set()   # Nodos en la pila de recursión actual
        
        def has_cycle(u):
            visited.add(u)
            rec_stack.add(u)
            
            for v in adj.get(u, []):
                if v not in visited:
                    if has_cycle(v):
                        return True
                elif v in rec_stack:
                    # Si el vecino está en la pila actual, hay un ciclo
                    return True
            
            rec_stack.remove(u)
            return False

        # Verificar cada tarea como punto de inicio
        for task in self.all_tasks:
            if task not in visited:
                if has_cycle(task):
                    raise Exception(f"Semantic Error: Infinite loop detected in workflow starting from task '{task}'.")

    def visitTask(self, ctx):
        """Marca el inicio de una tarea para que las transiciones internas sepan su origen."""
        task_name = ctx.ID().getText()
        self.current_task = task_name
        self.last_task_defined = task_name
        result = self.visitChildren(ctx)
        self.current_task = None
        return result

    def visitTransition(self, ctx):
        """Valida que la tarea destino exista y registra la conexión para el análisis de ciclos."""
        target_task = ctx.ID().getText()
        if target_task not in self.defined_tasks:
            raise Exception(f"Semantic Error: Transition to undefined task '{target_task}'.")
        
        # El origen es la tarea actual o la última definida (si la transición es global)
        source_task = self.current_task if self.current_task else self.last_task_defined
        if source_task:
            self.transitions.append((source_task, target_task))
            
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx):
        """Registra la variable en la tabla de símbolos al momento de asignarle un valor."""
        var_name = ctx.ID().getText()
        self.visit(ctx.expression())
        self.symbol_table.declare(var_name, 'int')

    def visitInputStmt(self, ctx):
        """Registra la variable cuando se pide por entrada de usuario."""
        var_name = ctx.ID().getText()
        self.symbol_table.declare(var_name, 'int')

    def visitPrimary(self, ctx):
        """Valida que las variables utilizadas en expresiones hayan sido declaradas previamente."""
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name == 'estado': # Variable reservada permitida por el ejemplo del profesor
                return
            if not self.symbol_table.exists(var_name):
                raise Exception(f"Semantic Error: Variable '{var_name}' not defined.")
        return self.visitChildren(ctx)
