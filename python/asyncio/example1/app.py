import asyncio
import random
import time
from pprint import pprint
from typing import AsyncIterable

from req_http import http_get, http_get_sync

MAX_POKEMON = 898


def get_random_pokemon_name_sync():
    pokemon_id = random.randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon["name"])


async def get_random_pokemon_name():
    pokemon_id = random.randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name


def main() -> None:
    """Performs synchronous operations"""

    start_time = time.perf_counter()
    for _ in range(20):
        pokemon_name = get_random_pokemon_name_sync()
        print(f"{pokemon_name=}")
    end_time = time.perf_counter()
    print(f"Performance: {end_time-start_time}")


async def main_async() -> None:
    """Performs asynchronous operations"""

    start_time = time.perf_counter()
    # for _ in range(20):
    #     pokemon_name = await get_random_pokemon_name()
    #     print(f"{pokemon_name=}")

    # Asynchronous concurrently
    # result = await asyncio.gather(*[get_random_pokemon_name() for _ in range(20)])
    # pprint(result)

    # Asynchronous for loop
    # async for name in next_pokemon(20):
    #     print(name)

    # Asynchronous for list comprehension
    names = [name async for name in next_pokemon(20)]
    pprint(names)

    end_time = time.perf_counter()
    print(f"Performance: {end_time-start_time}")


if __name__ == "__main__":
    # main()
    print()
    print()
    asyncio.run(main_async())
