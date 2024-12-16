from time import perf_counter
from c_prime_finder import c_prime_finder
from py_prime_finder import py_prime_finder


def main():
    n = 10000

    c_start: float = perf_counter()
    result = c_prime_finder(n)
    c_end: float = perf_counter()

    py_start: float = perf_counter()
    result = py_prime_finder(n)
    py_end: float = perf_counter()

    print('Time elapsed (C):', c_end-c_start)
    print('Time elapsed (Python):', py_end-py_start)


if __name__ == '__main__':
    main()
