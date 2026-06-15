import sys
import unittest
import io

def main():
    print("==================================================")
    print("Running Competition Tests...")
    print("==================================================\n")
    
    solved_count = 0
    total_problems = 10
    
    for i in range(1, 11):
        module_name = f"tests.test_problem_{i}"
        try:
            suite = unittest.defaultTestLoader.loadTestsFromName(module_name)
            # Run the test suite quietly
            stream = io.StringIO()
            runner = unittest.TextTestRunner(stream=stream, verbosity=0)
            result = runner.run(suite)
            
            passed = result.testsRun - len(result.failures) - len(result.errors)
            total = result.testsRun
            
            if result.wasSuccessful():
                print(f"Problem {i:02d}: PASSED ({passed}/{total} cases)")
                solved_count += 1
            else:
                print(f"Problem {i:02d}: FAILED ({passed}/{total} cases)")
                # Print details of the failed and crashed test cases in ASCII
                for test_case, tb in result.failures:
                    method_name = test_case._testMethodName
                    err_msg = tb.strip().split('\n')[-1]
                    print(f"  [X] {method_name}: {err_msg}")
                for test_case, tb in result.errors:
                    method_name = test_case._testMethodName
                    err_msg = tb.strip().split('\n')[-1]
                    print(f"  [!] {method_name} (CRASHED): {err_msg}")
                print()  # Add an extra newline for readability spacing
        except Exception as e:
            print(f"Problem {i:02d}: ERROR loading tests ({e})\n")
            
    print("==================================================")
    print(f"TOTAL SCORE: {solved_count} / {total_problems} problems solved")
    print("==================================================")
    
    sys.exit(0 if solved_count == total_problems else 1)

if __name__ == "__main__":
    main()
