def read_file(path, *funcs):
    with open(path, 'r') as inp:
        res = []
        for i, line in enumerate(inp.readlines()):
            res.append(funcs[i](line.rstrip()))
    return res


def read_lst_file(path, func, sep=" "):
    with open(path, 'r') as inp:
        lst = [func(i) for i in inp.readline().split(sep=sep)]
    return lst


def read_n_pairs_file(path):
    with open(path, 'r') as inp:
        n = int(inp.readline())
        lst = []
        for _ in range(n):
            a, b = map(int, inp.readline().split())
            lst.append((a, b))
    return n, lst


def read_lst_value_file(path, func):
    with open(path, 'r') as inp:
        lst = [func(i) for i in inp.readline().split()]
        v = int(inp.readline())
    return lst, v


def write_file(path, ans):
    with open(path, 'w') as out:
        print(ans, file=out, end='')


def write_lst_file(path, lst, sep=" "):
    with open(path, 'w') as out:
        print(*lst, file=out, sep=sep, end='')


def write_line_lst_line_file(path, line, lst, sep=" "):
    with open(path, 'w') as out:
        print(line, file=out)
        print(*lst, file=out, sep=sep, end='')