import os
from multiprocessing import Pool


def worker(num: int) -> int:
    pid = os.getppid()
    print(f"Processing for {num} in process: {pid}")
    result = num**num
    print(f"Completed processing for {num} in process: {pid}")
    return result


if __name__ == "__main__":
    with Pool(processes=6) as p:
        print(p.map(worker, [1, 2, 3, 4, 5, 6]))
