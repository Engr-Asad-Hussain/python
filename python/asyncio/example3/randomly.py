import asyncio
import pprint
import random
import time

# ANSI Color-Code
colors = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def make_random(index: int, threshold: int = 6) -> int:
    print(colors[index + 1] + f"Initiated make random [{index}] ...")
    i = random.randint(0, 10)
    while i < threshold:
        print(
            colors[index + 1] + f"... make random [{index} == {i}] too low; retrying."
        )
        await asyncio.sleep(1)
        i = random.randint(0, 10)

    print(colors[index + 1] + f"Finished make random! [{index} == {i}]" + colors[0])
    return i


async def main():
    result = await asyncio.gather(*[make_random(i) for i in range(3)])
    print()
    pprint.pprint(result)


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"Total time: {elapsed:0.2F}")


"""
This program uses one main coroutine, make_random(), and runs it concurrently across 
3 different inputs. Most programs will contain small, modular coroutines and one wrapper function 
that serves to chain each of the smaller coroutines together. main() is then used to gather 
tasks (futures) by mapping the central coroutine across some iterable or pool.

In this miniature example, the pool is range(3). In a fuller example presented 
later, it is a set of URLs that need to be requested, parsed, and processed concurrently, 
and main() encapsulates that entire routine for each URL.

While “making random integers” (which is CPU-bound more than anything) is maybe not the 
greatest choice as a candidate for asyncio, its the presence of asyncio.sleep() in the 
example that is designed to mimic an IO-bound process where there is uncertain wait 
time involved. For example, the asyncio.sleep() call might represent sending and receiving 
not-so-random integers between two clients in a message application.
"""
