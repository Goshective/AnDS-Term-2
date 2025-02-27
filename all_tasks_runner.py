import sys
import os
import glob
from tabulate import tabulate


PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PATH)
LABS_NAMES = [f'Lab{i}' for i in range(1, 9)]


def parse_info_from_folder(file):
    task_directory = os.path.basename(os.path.dirname(file))
    txtf_directory = os.path.dirname(file)
    task_num = int(task_directory[4:])

    inp_path = os.path.join(txtf_directory, 'input.txt')
    out_path = os.path.join(txtf_directory, 'output.txt')

    table_pairs = []
    with open(inp_path, 'r') as inp, open(out_path, 'r') as out:
        inp_lines = inp.readlines()
        out_lines = out.readlines()
        mini_len, maxi_len = [f(len(inp_lines), len(out_lines)) for f in (min, max)]
        for i in range(mini_len):
            table_pairs.append([inp_lines[i].rstrip(), out_lines[i].rstrip()])
        for i in range(mini_len, maxi_len):
            if i >= len(inp_lines):
                table_pairs.append(["", out_lines[i].rstrip()])
            else:
                table_pairs.append([inp_lines[i].rstrip(), ""])
    
    return task_num, tabulate(table_pairs, headers=['Input', 'Output'], tablefmt='orgtbl')


def run_tasks(labs_names=LABS_NAMES):
    for lab_name in labs_names:
        lab_path = os.path.join(PATH, lab_name)

        if os.path.exists(lab_path):
            for file in glob.iglob(f"{lab_name}/*/main.py"):

                os.system("python " + file)

                task_num, table_inp_out = parse_info_from_folder(file)
                print()
                print(f"{lab_name}. Task {task_num}")
                print()
                print(table_inp_out)


if __name__ == '__main__':
    run_tasks()