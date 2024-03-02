""" How to convert blocking code into non-blocking asynchronous concurrent"""
import asyncio
import time

import requests


async def counter(until: int = 10):
    now = time.perf_counter()
    print("Started counter")
    for i in range(0, until):
        last = now
        await asyncio.sleep(0.01)
        now = time.perf_counter()
        print(f"{i}. was asleep for {now-last}s.")


def send_request(url: str) -> int:
    print("Sending HTTP request")
    response = requests.get(url)
    return response.status_code


async def send_async_request(url: str):
    """Create a separate thread to run this task"""

    return await asyncio.to_thread(send_request, url)


async def main():
    # task = asyncio.create_task(counter())
    # status_code = await send_async_request("https://www.arjancodes.com")
    # print(f"Got http response with status code: {status_code}")
    # await task

    status_code, _ = await asyncio.gather(
        send_async_request("https://arjancodes.com"), counter()
    )
    print(f"Got http response with status code: {status_code}")


if __name__ == "__main__":
    asyncio.run(main())
