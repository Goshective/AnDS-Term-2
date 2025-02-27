import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..'))

from all_tasks_runner import run_tasks


run_tasks(['Lab1'])