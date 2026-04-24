#!/usr/bin/env python3
"""
MiniCompiladorWorkflow - Main entry point
"""

import sys
from antlr4 import *
from generated.WhileLangLexer import WhileLangLexer
from generated.WhileLangParser import WhileLangParser
from semantic_analyzer.semantic_visitor import SemanticVisitor
from codegen.python_generator import PythonGenerator

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        input_text = f.read()

    # Lexical and syntactic analysis
    input_stream = InputStream(input_text)
    lexer = WhileLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WhileLangParser(token_stream)
    tree = parser.program()

    # Semantic analysis
    semantic_visitor = SemanticVisitor()
    semantic_visitor.visit(tree)

    # Code generation
    code_generator = PythonGenerator()
    output_code = code_generator.generate(tree)

    # Write output
    with open('output_program.py', 'w') as f:
        f.write(output_code)

    print("Compilation successful. Output written to output_program.py")

if __name__ == "__main__":
    main()