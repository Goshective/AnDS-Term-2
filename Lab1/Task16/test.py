import unittest
import sys
import os
from random import randint

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab1.Task16.main import solution
from test_utils import (
    ConsoleTimeMemory as TM, 
    get_task_name,
    MB
)


class TestCaseInsertionSort(unittest.TestCase):
    def test_1(self):
        # given
        inp = [
            [0, 183, 163, 173, 181],
            [183, 0, 165, 172, 171],
            [163, 165, 0, 189, 302],
            [173, 172, 189, 0, 167],
            [181, 171, 302, 167, 0]]
        expected_res = (666, [4, 5, 2, 3, 1])
        # when
        res = solution(inp)
        # then
        self.assertEqual(res, expected_res)

    def check_time_memory_limit(self, res_time, res_memory):
        # given
        expected_memory = 256 * MB
        expected_time = 1.05
        # when
        # then
        self.assertLessEqual(res_time, expected_time)
        self.assertLessEqual(res_memory, expected_memory)
    
    def test_should_fit_time_memory_limit(self):
        # given
        mat = []
        for _ in range(13):
            mat.append([0]*13)

        for i in range(13):
            for j in range(i+1, 13):
                mat[i][j] = mat[j][i] = randint(0, 40)

        test_data = [
            ('3 элемента', [
                [0, 10, 20],
                [10, 0, 30],
                [20, 30, 0],
            ]),
            ('5 элементов', [
                [0, 183, 163, 173, 181],
                [183, 0, 165, 172, 171],
                [163, 165, 0, 189, 302],
                [173, 172, 189, 0, 167],
                [181, 171, 302, 167, 0]
            ]),
            ('13 элементов', mat)]

        
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