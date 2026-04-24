# MiniCompiladorWorkflow

A mini compiler for a simple workflow language (WhileLang) that compiles to Python.

## Features

- Lexical and syntactic analysis using ANTLR4
- Semantic analysis with symbol table
- Code generation to Python

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Generate ANTLR files: `antlr4 -Dlanguage=Python3 gramatica.g4 -o generated`
3. Run: `python main.py input.txt`

## Structure

- `main.py`: Main entry point
- `gramatica.g4`: ANTLR grammar
- `generated/`: ANTLR generated files
- `semantic_analyzer/`: Semantic analysis modules
- `codegen/`: Code generation modules
- `tests/`: Test cases
- `docs/`: Documentation