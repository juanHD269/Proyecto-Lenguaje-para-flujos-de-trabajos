#!/usr/bin/env python3
import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from generated.gramaticaLexer import gramaticaLexer
from generated.gramaticaParser import gramaticaParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor
from codegen.python_generator import PythonGenerator
from codegen.ir_generator import IRGenerator

import time

class BailErrorListener(ErrorListener):
    def __init__(self, phase):
        self.phase = phase

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"\n[!] ERROR DETECTED IN {self.phase.upper()} PHASE")
        print(f"    Location: Line {line}, Column {column}")
        print(f"    Message: {msg}")
        raise Exception(f"[{self.phase} Error] at {line}:{column}: {msg}")

def select_test_file():
    valid_dir = os.path.join('tests', 'valid')
    invalid_dir = os.path.join('tests', 'invalid')
    
    files = []
    if os.path.exists(valid_dir):
        for f in sorted(os.listdir(valid_dir)):
            if f.endswith('.wf'):
                files.append(('VALID', os.path.join(valid_dir, f)))
    
    if os.path.exists(invalid_dir):
        for f in sorted(os.listdir(invalid_dir)):
            if f.endswith('.wf'):
                files.append(('INVALID', os.path.join(invalid_dir, f)))

    if not files:
        print("No test files (.wf) found in tests/valid or tests/invalid.")
        return 'input.txt' if os.path.exists('input.txt') else None

    print("\n" + "="*60)
    print("      MINI-COMPILADOR WORKFLOW - TEST MENU")
    print("="*60)
    print(f"{'#':<3} | {'TYPE':<8} | {'FILE NAME'}")
    print("-" * 60)
    
    for i, (ftype, path) in enumerate(files):
        fname = os.path.basename(path)
        print(f"{i+1:<3} | {ftype:<8} | {fname}")
    
    print("-" * 60)
    print(f"{0:<3} | {'-':<8} | Usar input.txt (archivo raíz)")
    print("=" * 60)

    try:
        choice = int(input("\nSeleccione el número del archivo a compilar: "))
        if choice == 0:
            return 'input.txt'
        if 1 <= choice <= len(files):
            return files[choice-1][1]
    except ValueError:
        pass
    
    print("Selección no válida. Usando input.txt por defecto.")
    return 'input.txt'

def main():
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
    else:
        input_file = select_test_file()
        if not input_file:
            print("Error: No se encontró ningún archivo para compilar.")
            sys.exit(1)

    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found.")
        sys.exit(1)

    start_time = time.time()
    with open(input_file, 'r', encoding='utf-8') as f:
        input_text = f.read()

    log_output = []
    print("\n" + "#"*60)
    print(f"Starting Compilation of: {input_file}")
    print("#"*60)

    try:
        # 1. Lexical Analysis
        p1_start = time.time()
        print("\n" + "+" + "-"*58 + "+")
        print("| PHASE 1: LEXICAL ANALYSIS (Tokenization)".ljust(59) + "|")
        print("+" + "-"*58 + "+")
        input_stream = InputStream(input_text)
        lexer = gramaticaLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(BailErrorListener("Lexical"))
        
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()
        
        print(f"[*] Analysis complete. Found {len(token_stream.tokens)} tokens.")
        print("    " + "-"*40)
        print("    ID   | TYPE            | TEXT            | LINE:COL")
        print("    " + "-"*40)
        for i in range(min(15, len(token_stream.tokens))):
            t = token_stream.tokens[i]
            if t.type != -1: # Skip EOF
                symbolic = lexer.symbolicNames[t.type]
                print(f"    {i:<4} | {symbolic:<15} | '{t.text.strip()}':<15 | {t.line}:{t.column}")
        if len(token_stream.tokens) > 15:
            print(f"    ... and {len(token_stream.tokens)-15} more tokens.")
        
        p1_end = time.time()
        print(f"\n[OK] Lexical Phase finished in {(p1_end-p1_start)*1000:.2f}ms")

        # 2. Syntactic Analysis
        p2_start = time.time()
        print("\n" + "+" + "-"*58 + "+")
        print("| PHASE 2: SYNTACTIC ANALYSIS (Parsing)".ljust(59) + "|")
        print("+" + "-"*58 + "+")
        parser = gramaticaParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(BailErrorListener("Syntactic"))
        tree = parser.program()
        
        print("[*] Parsing complete. Syntactic structure validated.")
        print("[*] AST Root: <program>")
        # Print a more readable tree structure
        tree_str = tree.toStringTree(recog=parser)
        print(f"[*] Parse Tree Preview: {tree_str[:120]}...")
        
        p2_end = time.time()
        print(f"\n[OK] Syntactic Phase finished in {(p2_end-p2_start)*1000:.2f}ms")

        # 3. Semantic Analysis
        p3_start = time.time()
        print("\n" + "+" + "-"*58 + "+")
        print("| PHASE 3: SEMANTIC ANALYSIS (Context Checking)".ljust(59) + "|")
        print("+" + "-"*58 + "+")
        semantic_visitor = SemanticVisitor()
        semantic_visitor.visit(tree)
        
        print(f"[*] Symbol Table Analysis:")
        vars_found = list(semantic_visitor.symbol_table.symbols.keys())
        print(f"    - Variables: {vars_found if vars_found else 'None'}")
        print(f"[*] Task Graph Analysis:")
        print(f"    - Defined Tasks: {list(semantic_visitor.defined_tasks)}")
        print(f"    - Workflow Transitions:")
        for u, v in semantic_visitor.transitions:
            print(f"      {u} ---> {v}")
        
        print("[*] Safety Checks:")
        print("    - Infinite Loop Check: PASSED (No cycles detected)")
        print("    - Undefined Task Check: PASSED")
        print("    - Scope/Declaration Check: PASSED")
        
        p3_end = time.time()
        print(f"\n[OK] Semantic Phase finished in {(p3_end-p3_start)*1000:.2f}ms")

        # 4. Intermediate Code Generation (IR)
        p4_start = time.time()
        print("\n" + "+" + "-"*58 + "+")
        print("| PHASE 4: INTERMEDIATE CODE GENERATION (TAC)".ljust(59) + "|")
        print("+" + "-"*58 + "+")
        ir_generator = IRGenerator()
        ir_code = ir_generator.generate(tree)
        
        print("[*] 3-Address Code (TAC) listing:")
        print("    " + "="*30)
        for line in ir_code.split('\n'):
            print(f"    {line}")
        print("    " + "="*30)
        
        p4_end = time.time()
        print(f"\n[OK] IR Generation finished in {(p4_end-p4_start)*1000:.2f}ms")

        # 5. Target Code Generation (Python)
        p5_start = time.time()
        print("\n" + "+" + "-"*58 + "+")
        print("| PHASE 5: PYTHON CODE GENERATION (Back-end)".ljust(59) + "|")
        print("+" + "-"*58 + "+")
        code_generator = PythonGenerator()
        output_code = code_generator.generate(tree)
        
        print(f"[*] Translation complete.")
        print(f"    - Functions generated: {len(code_generator.all_tasks)}")
        print(f"    - Global state variables: {list(code_generator.variables)}")
        print(f"[*] Code Preview (first 10 lines):")
        print("    " + "."*30)
        preview = "\n".join(output_code.split('\n')[:15])
        for line in preview.split('\n'):
            print(f"    {line}")
        print("    " + "."*30)
        
        p5_end = time.time()
        print(f"\n[OK] Code Generation finished in {(p5_end-p5_start)*1000:.2f}ms")

        # Finalizing
        with open('output_program.py', 'w', encoding='utf-8') as f:
            f.write(output_code)
        
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(f"COMPILATION LOG - {time.ctime()}\n")
            f.write("-" * 50 + "\n")
            f.write(f"Lexical tokens: {len(token_stream.tokens)}\n")
            f.write(f"Semantic tasks: {len(semantic_visitor.defined_tasks)}\n")
            f.write("-" * 50 + "\n\n")
            f.write("--- INTERMEDIATE CODE (TAC) ---\n")
            f.write(ir_code)

        total_time = (time.time() - start_time) * 1000
        print("\n" + "#"*60)
        print(f"### COMPILATION SUCCESSFUL IN {total_time:.2f}ms ###")
        print(f"### Final Program: output_program.py".ljust(56) + " ###")
        print(f"### Analysis Report: output.txt".ljust(56) + " ###")
        print("#"*60 + "\n")

    except Exception as e:
        error_msg = str(e)
        # print(f"\n[FATAL ERROR] {error_msg}") # Already printed by listener
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(f"Compilation Failed:\n{error_msg}")
        sys.exit(1)

if __name__ == "__main__":
    main()
