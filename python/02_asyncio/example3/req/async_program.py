import asyncio
import pathlib
import re
import time
import urllib
import urllib.error
import urllib.parse
from pprint import pprint

import aiofiles
import aiohttp

HREF_RE = re.compile(r'href="(.*?)"')
colors = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def async_make_request_builtin(url: str) -> str | None:
    async with aiohttp.ClientSession() as session:
        print(colors[1] + f"Requesting to {url}" + colors[0])
        try:
            resp = await session.request(method="GET", url=url)
            resp.raise_for_status()
            return await resp.text()
        except aiohttp.ClientResponseError as e:
            print(colors[2] + f"{e.status} | {url}" + colors[0])


def parse_html(url: str, html: str) -> list[str]:
    found_links: list[str] = []
    for link in HREF_RE.findall(html):
        abslink = urllib.parse.urljoin(url, link)
        found_links.append(abslink)
    return found_links


async def search_urls(url: str):
    html = await async_make_request_builtin(url)
    if html is not None:
        found_urls = parse_html(url, html)
    else:
        found_urls = []

    path = pathlib.Path(__file__).parent
    async with aiofiles.open(path.joinpath("foundurls.txt"), mode="a") as file:
        for url in found_urls:
            await file.write(url + "\n")


async def main():
    path = pathlib.Path(__file__).parent
    with open(path.joinpath("urls.txt"), mode="r") as file:
        urls = [line.strip() for line in file]
        file.close()

    pprint(urls)
    print()
    await asyncio.gather(*[search_urls(url) for url in urls])


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Total time passed: {elapsed:0.2F}s")
