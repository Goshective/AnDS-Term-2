import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab1.utils import read_n_table_file, write_value_lst_file


def solution(mat):
    res = None
    res_path = []
    n = len(mat)

    for start_i in range(n):
        cache = []
        for _ in range(n):
            cache.append([])
            for _ in range(n):
                cache[-1].append([None, None])

        stack = [(start_i, 0, set(range(n)) - {start_i}, [start_i])]
        while stack:
            i, dist, left, path = stack.pop()
            for j in left:
                if cache[i][j][0] is None or dist < cache[i][j][0]:
                    cache[i][j][0] = dist + mat[i][j]
                    cache[i][j][1] = path + [j]
                    new_left = left.copy()
                    new_left.remove(j)

                    stack.append((j, dist + mat[i][j], new_left, cache[i][j][1]))

            if not left:
                if res is None or dist < res:
                    res = dist
                    res_path = path

    for i in range(n):
        res_path[i] += 1
    return res, res_path


def main():
    _, mat = read_n_table_file(os.path.join(PATH, 'input.txt'))
    res_val, res_path = solution(mat)
    write_value_lst_file(os.path.join(PATH, 'output.txt'), res_val, res_path)


if __name__ == "__main__":
    main()