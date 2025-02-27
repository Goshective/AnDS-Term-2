import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab1.utils import read_n_pairs_file, write_file


cache_start = {}

def lec_from_i(lst, i):
    if i in cache_start:
        return cache_start[i]
    if i == len(lst) - 1:
        cache_start[i] = 1
        return 1
    maxi = 0
    for idx in range(i+1, len(lst)):
        if lst[i][1] <= lst[idx][0]:
            res = lec_from_i(lst, idx)
            maxi = max(maxi, res + 1)
    cache_start[i] = maxi
    return maxi


# def lec_from_i_dp(lst):
#     stack = [(0, 1, 1)]
#     n = len(lst)
#     cache_start = [0] * n
#     while stack:
#         i, maxi, k = stack.pop()
#         if cache_start[i] != 0:
#             return cache_start[i]
#         maxi = 0
#         for idx in range(i+1, len(lst)):
#             res = lec_from_i(lst, idx)
#             stack.append(idx, n)
#             maxi = max(maxi, res + 1)
#         cache_start[i] = maxi


def solution(lst):
    lst.sort(key=lambda x: x[0])
    res = 1
    for i in range(len(lst)):
        res = max(lec_from_i(lst, i), res)
    return res


def main():
    n, lst = read_n_pairs_file(os.path.join(PATH, 'input.txt'))
    res = solution(lst)
    write_file(os.path.join(PATH, 'output.txt'), res)


if __name__ == "__main__":
    main()