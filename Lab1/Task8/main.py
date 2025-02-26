import os
import sys

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PATH, '..', '..'))

from Lab1.utils import read_len_lst_file, write_lst_file


def insertion_sort(n, lst):
    if n <= 1: return

    for i in range(1, n):
        key_elem = lst[i]
        j = i - 1

        while j >= 0 and key_elem < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key_elem
    return

def main():
    n, lst = read_len_lst_file(os.path.join(PATH, 'txtf', 'input.txt'), int)
    insertion_sort(n, lst)
    write_lst_file(os.path.join(PATH, 'txtf', 'output.txt'), lst)


if __name__ == "__main__":
    main()