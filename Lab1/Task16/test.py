import unittest
import sys
import os
from random import shuffle

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab1.Task8.main import solution
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestCaseInsertionSort(unittest.TestCase):
    def test_1(self):
        # given
        inp = [(1, 5), (2, 3), (3, 4)]
        expected_res = 2
        # when
        res = solution(inp)
        # then
        self.assertEqual(res, expected_res)

    def test_2(self):
        # given
        inp = [(5, 10)]
        expected_res = 1
        # when
        res = solution(inp)
        # then
        self.assertEqual(res, expected_res)

    def check_time_memory_limit(self, res_time, res_memory):
        # given
        expected_memory = 256 * MB
        expected_time = 2
        # when
        # then
        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        # given
        test_data = [('3 элемента', [(1, 5), (2, 3), (3, 4)]),
                     ('100 элементов', [(i, i+2) for i in range(100)]),
                     ('1000 элементов', [(i, i+3) for i in range(1000)]),
                     ('1000 элементов (пересечение)', [(i, 3*(i+1)) for i in range(1000)])]

        
        print()
        print('-'*55)
        print(get_task_name(PATH))

        for test_name, input_by_size in test_data:
            # when
            res_time = TM.count_time(solution, input_by_size)
            res_memory = TM.count_memory(solution, input_by_size)

            TM.output_design(test_name, res_time, res_memory)

            # then
            self.check_time_memory_limit(res_time, res_memory)
        

        print('-'*55)


if __name__ == "__main__":
    unittest.main()