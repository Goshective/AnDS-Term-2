import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..'))

from all_tests_runner import run_tests


run_tests(['Lab1'])