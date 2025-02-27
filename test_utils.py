import os
import time
import tracemalloc


MB = 1024**2


class ConsoleTimeMemory:
    @staticmethod
    def output_design(test_name, res_time, res_memory):
            if res_memory < 1024:
                out_mem = f'{res_memory} Байт'
            elif res_memory < 1024**2:
                out_mem = f'{round(res_memory / 1024, 1)} Килобайт'
            else:
                out_mem = f'{round(res_memory / (1024**2), 1)} Мегабайт'

            print()
            print(f"Тест {test_name}:")
            print("Время работы: %s секунд " % (round(res_time, 6)), end='\n')
            print("Затрачено памяти:", out_mem)
    
    @staticmethod
    def count_time(func, *args):
        t_start = time.perf_counter()
        func(*args)
        res_time = time.perf_counter() - t_start
        return res_time

    @staticmethod
    def count_memory(func, *args):
        tracemalloc.start()
        func(*args)
        memory = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        return memory


def get_task_name(path):
    lab_directory = os.path.basename(os.path.dirname(path))
    task_directory = os.path.basename(path)
    task_num = int(task_directory[4:])

    return f'{lab_directory}. Task {task_num}'