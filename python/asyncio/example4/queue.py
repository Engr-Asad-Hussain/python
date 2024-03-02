import random
from collections import deque

# ANSI Color-Code
colors = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
    "\033[34m",  # Blue
    "\033[32m",  # Yellow
    "\033[45m",  # Blink
)


def generate_id(length: int = 6) -> int:
    return random.randint(1, length)


def task(name: str, work_queue: deque[int]) -> None:
    if work_queue:
        count = work_queue.pop()
        total = 0
        id = generate_id()
        print(colors[id] + f"Task {name} started!" + colors[0])
        for _ in range(count):
            total += 1
        print(colors[id] + f"Task {name} total {total}" + colors[0])
    else:
        print(f"Task {name} is empty!")


def main():
    # Create a task-queue
    works: deque[int] = deque()
    works.extend([1, 2, 3, 4, 5])

    tasks = [("One", works, task), ("Two", works, task), ("Three", works, task)]
    for name, deq, fn in tasks:
        # print(f"{name=}")
        fn(name, deq)


if __name__ == "__main__":
    main()
