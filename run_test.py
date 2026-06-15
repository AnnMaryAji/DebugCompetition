import sys
import unittest
import io

def main():
    problem = None
    
    # 1. Parse command line argument if present
    if len(sys.argv) > 1:
        try:
            problem = int(sys.argv[1])
            if problem < 1 or problem > 10:
                print("Error: Problem number must be between 1 and 10.")
                sys.exit(1)
        except ValueError:
            print("Error: Argument must be a number between 1 and 10.")
            sys.exit(1)
    else:
        # 2. Prompt user using input()
        try:
            user_input = input("Enter problem number to run (1-10): ").strip()
            problem = int(user_input)
            if problem < 1 or problem > 10:
                print("Error: Problem number must be between 1 and 10.")
                sys.exit(1)
        except (KeyboardInterrupt, SystemExit):
            print("\nExiting.")
            sys.exit(0)
        except ValueError:
            print("Error: Input must be a number between 1 and 10.")
            sys.exit(1)

    # 3. Load and run the specific test suite quietly
    print(f"\nRunning tests for Problem {problem}...")
    print("--------------------------------------------------")
    module_name = f"tests.test_problem_{problem}"
    try:
        suite = unittest.defaultTestLoader.loadTestsFromName(module_name)
        stream = io.StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=0)
        result = runner.run(suite)
        
        passed = result.testsRun - len(result.failures) - len(result.errors)
        total = result.testsRun
        
        if result.wasSuccessful():
            print(f"Problem {problem:02d}: PASSED ({passed}/{total} cases)")
            sys.exit(0)
        else:
            print(f"Problem {problem:02d}: FAILED ({passed}/{total} cases)")
            for test_case, tb in result.failures:
                method_name = test_case._testMethodName
                err_msg = tb.strip().split('\n')[-1]
                print(f"  [X] {method_name}: {err_msg}")
            for test_case, tb in result.errors:
                method_name = test_case._testMethodName
                err_msg = tb.strip().split('\n')[-1]
                print(f"  [!] {method_name} (CRASHED): {err_msg}")
            sys.exit(1)
    except Exception as e:
        print(f"Error loading tests for Problem {problem}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
