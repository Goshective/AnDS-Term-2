import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab1.utils import read_n_table_file, write_len_lst_file


def solution(mat):
    cache = []
    n = len(mat)
    for _ in range(n):
        cache.append([None]*n)

    stack = [(0, 0, set(range(1, n)), [0])]
    while stack:
        i, dist, left, path = stack.pop()
        for j in left:
            if cache[i][j] is None or dist < cache[i][j]:
                dist += mat[i][j]
                cache[i][j] = dist
                new_left = left.copy()
                new_left.remove(j)
                stack.append((j, dist, new_left))

    return cache[n-1][n-1]


def main():
    n, mat = read_n_table_file(os.path.join(PATH, 'input.txt'))
    res = solution(mat)
    write_len_lst_file(os.path.join(PATH, 'output.txt'), res)


if __name__ == "__main__":
    main()