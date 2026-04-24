class SemanticError(Exception):
    pass

class UndeclaredVariableError(SemanticError):
    pass

class RedeclaredVariableError(SemanticError):
    pass