import sys
import unittest

def main():
    # Discover and run all tests in the 'tests' directory
    suite = unittest.defaultTestLoader.discover('tests', pattern='test_problem_*.py')
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)

if __name__ == "__main__":
    main()
