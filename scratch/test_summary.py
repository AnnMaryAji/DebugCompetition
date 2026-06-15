import unittest
import sys

def main():
    print("Gathering test execution stats...")
    print("--------------------------------------------------")
    
    total_passed = 0
    total_cases = 0
    solved_problems = 0
    
    for i in range(1, 11):
        module_name = f"tests.test_problem_{i}"
        try:
            suite = unittest.defaultTestLoader.loadTestsFromName(module_name)
            runner = unittest.TextTestRunner(verbosity=0)
            result = runner.run(suite)
            
            passed = result.testsRun - len(result.failures) - len(result.errors)
            total = result.testsRun
            
            total_passed += passed
            total_cases += total
            
            is_solved = (passed == total)
            if is_solved:
                solved_problems += 1
                
            status = "PASSED" if is_solved else "FAILED"
            print(f"Problem {i:02d}: {status} ({passed}/{total} cases passed)")
            
            if not is_solved:
                # Print why it failed (syntax vs logic)
                if len(result.errors) > 0:
                    print(f"    -> Had errors (compile/import/syntax issues)")
                elif len(result.failures) > 0:
                    print(f"    -> Had failures (logical bugs)")
        except Exception as e:
            print(f"Problem {i:02d}: ERROR loading suite ({e})")
            
    print("--------------------------------------------------")
    print(f"TOTAL TESTS PASSED: {total_passed} / {total_cases}")
    print(f"TOTAL PROBLEMS SOLVED: {solved_problems} / 10")

if __name__ == "__main__":
    main()
