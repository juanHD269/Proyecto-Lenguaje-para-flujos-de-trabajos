# Diagramas Mermaid

```mermaid
graph TD;
    A[Input] --> B[Lexer];
    B --> C[Parser];
    C --> D[Semantic Analysis];
    D --> E[Code Generation];
    E --> F[Output];
```