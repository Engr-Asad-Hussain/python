import os
from multiprocessing import Process


def factorial(n: int):
    # n! = n(n-1)(n-2) ...
    if n == 0:
        return 1
    return n * factorial(n - 1)


def worker(num: int) -> None:
    pid = os.getpid()
    print(f"Worker Process ID is: {pid}")
    print(f"The factorial of {num} is: {factorial(num)}")


if __name__ == "__main__":
    processes = [Process(target=worker, args=(num,)) for num in (100, 50, 10, 0)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
