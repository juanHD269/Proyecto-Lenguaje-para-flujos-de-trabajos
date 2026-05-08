import os
import subprocess
import sys

def run_test(file_path, expected_success=True):
    print(f"Testing: {os.path.basename(file_path)} ... ", end="")
    try:
        result = subprocess.run(
            [sys.executable, 'main.py', file_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        actual_success = (result.returncode == 0)
        if actual_success == expected_success:
            print("PASS")
            return True
        else:
            print("FAIL")
            return False
    except Exception as e:
        print(f"ERROR ({str(e)})")
        return False

def main():
    valid_dir = os.path.join('tests', 'valid')
    invalid_dir = os.path.join('tests', 'invalid')
    total_tests = 0
    passed_tests = 0
    print("=== RUNNING VALID TESTS ===")
    if os.path.exists(valid_dir):
        files = sorted([f for f in os.listdir(valid_dir) if f.endswith('.wf')])
        for f in files:
            total_tests += 1
            if run_test(os.path.join(valid_dir, f), True):
                passed_tests += 1
    print("\n=== RUNNING INVALID TESTS ===")
    if os.path.exists(invalid_dir):
        files = sorted([f for f in os.listdir(invalid_dir) if f.endswith('.wf')])
        for f in files:
            total_tests += 1
            if run_test(os.path.join(invalid_dir, f), False):
                passed_tests += 1
    print(f"\nSummary: {passed_tests}/{total_tests} tests passed.")

if __name__ == "__main__":
    main()
