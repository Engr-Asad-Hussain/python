import asyncio
import random
import sys
import time

colors = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(colors[3] + "Starting Part1" + colors[0])
    print(f"... Part1 ({n}) sleeps for {i}s.")
    await asyncio.sleep(i)
    result = f"result {n} - 1"
    print(f"... Returning Part1 ({n}) == {result}")
    return result


async def part2(n: int, args: str) -> str:
    i = random.randint(0, 10)
    print(colors[2] + "Starting Part2" + colors[0])
    await asyncio.sleep(i)
    result = f"result{n} - 2 derived from {args}"
    print(f"... Returning Part2 ({n, args}) == {result}")
    return result


async def chain(n: int) -> None:
    # start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    # end = time.perf_counter() - start
    # print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")


async def main():
    args = [1, 2, 3]
    print(f"{args=}")
    print()
    await asyncio.gather(*[chain(n) for n in args])


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print()
    print(f"Total time elapsed: {elapsed:0.2F}s")
