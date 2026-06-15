import sys
import time
import unittest
import io

def main():
    print("==================================================")
    print("[-] Timing Solutions (Average of 10 Runs) ...")
    print("==================================================")
    
    all_passed = True
    for i in range(1, 11):
        module_name = f"tests.test_problem_{i}"
        try:
            suite = unittest.defaultTestLoader.loadTestsFromName(module_name)
            
            # Warm-up and validation run
            buffer = io.StringIO()
            runner = unittest.TextTestRunner(stream=buffer, verbosity=0)
            result = runner.run(suite)
            
            if not result.wasSuccessful():
                print(f"Problem {i:02d}: [X] FAILED tests (cannot time buggy code)")
                all_passed = False
                continue
                
            # Time 10 consecutive runs
            start_time = time.perf_counter()
            runs = 10
            for _ in range(runs):
                runner.run(suite)
            end_time = time.perf_counter()
            
            avg_ms = ((end_time - start_time) / runs) * 1000
            print(f"Problem {i:02d}:  PASSED - Average Time: {avg_ms:.3f} ms")
            
        except Exception as e:
            print(f"Problem {i:02d}: [!] ERROR loading tests ({e})")
            all_passed = False

    print("==================================================")
    if not all_passed:
        print("[!] Some problems failed their tests. Please fix all bugs to get timing results.")
        sys.exit(1)
    else:
        print("[Success] All solutions timed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
