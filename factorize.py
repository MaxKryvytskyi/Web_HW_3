from args import get_cpu_count
from time import time
import multiprocessing

def factorize_number(number):
    list_division = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_division.append(i)
    return list_division


def factorize(*numbers):
    result = []
    for number in numbers:
        result.append(factorize_number(number))
    return result


if __name__ == '__main__':
    numbers = [i * 1000 for i in range (1, 500)]
    print("start")

    # Synchron
    start_time = time()
    results = factorize(*numbers)
    end_time = time()
    print(f"Synchron calculation is done {end_time - start_time} sec.")

    # Multiprocesing
    pool = multiprocessing.Pool(processes=get_cpu_count())
    start_time = time()
    results = pool.map(factorize_number, numbers)
    end_time = time()
    print(f"Multi-process calculation is done {end_time - start_time} sec.")
