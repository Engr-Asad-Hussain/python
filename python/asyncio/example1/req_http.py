import asyncio
from typing import Any

import requests


def http_get_sync(url: str) -> dict[str, Any]:
    response = requests.get(url)
    return response.json()


async def http_get(url: str) -> dict[str, Any]:
    return await asyncio.to_thread(http_get_sync, url)
