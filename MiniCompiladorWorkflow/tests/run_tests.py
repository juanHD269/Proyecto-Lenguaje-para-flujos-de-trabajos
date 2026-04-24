#!/usr/bin/env python3
"""
Test runner for MiniCompiladorWorkflow
"""

import os
import subprocess

def run_test(file_path):
    # Run main.py on the file
    result = subprocess.run(['python', 'main.py', file_path], capture_output=True, text=True)
    return result.returncode == 0, result.stdout, result.stderr

def main():
    valid_dir = 'tests/valid'
    invalid_dir = 'tests/invalid'

    print("Running valid tests...")
    for file in os.listdir(valid_dir):
        if file.endswith('.wf'):
            success, out, err = run_test(os.path.join(valid_dir, file))
            print(f"{file}: {'PASS' if success else 'FAIL'}")

    print("Running invalid tests...")
    for file in os.listdir(invalid_dir):
        if file.endswith('.wf'):
            success, out, err = run_test(os.path.join(invalid_dir, file))
            print(f"{file}: {'PASS' if not success else 'FAIL'}")  # Invalid should fail

if __name__ == "__main__":
    main()