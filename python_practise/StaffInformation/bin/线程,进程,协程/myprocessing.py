from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import time
pool = ProcessPoolExecutor(4)

def func(arg):
    time.sleep(1)
    print(multiprocessing.current_process().name,arg)
if __name__ == '__main__':
    for i in range(20):
        pool.submit(func,i)