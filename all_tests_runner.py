import unittest
import os
import sys


PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PATH)
LABS_NAMES = [f'Lab{i}' for i in range(1, 5)]


def run_tests(labs_names=LABS_NAMES):
    tasks_names = [f"Task{i}" for i in range(1, 40)]
    # Collect all test files
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()

    for lab in labs_names:
        for task_folder_name in tasks_names:
            lab_path = os.path.join(lab, task_folder_name, 'tests')

            if os.path.exists(lab_path):
                # Load tests from test.py files
                test_file = os.path.join(lab_path, 'test.py')
                
                if os.path.isfile(test_file):
                    tests = test_loader.loadTestsFromName(f'{lab}.{task_folder_name}.tests.test')
                    test_suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(test_suite)

if __name__ == '__main__':
    run_tests()