import pathlib
import re
import time
import urllib
import urllib.error
import urllib.parse
from pprint import pprint

import requests

HREF_RE = re.compile(r'href="(.*?)"')
colors = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


def make_request(url: str) -> str:
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.text
    except requests.exceptions.RequestException as e:
        print(colors[2] + f"400 | {url}" + colors[0])
        raise e


def parse_html(url: str, html: str) -> list[str]:
    found_links: list[str] = []
    for link in HREF_RE.findall(html):
        abslink = urllib.parse.urljoin(url, link)
        found_links.append(abslink)
    return found_links


def main():
    path = pathlib.Path(__file__).parent
    with open(path.joinpath("urls.txt"), mode="r") as file:
        urls = [line.strip() for line in file]
        file.close()

    pprint(urls)
    with open(path.joinpath("foundurls.txt"), mode="w") as file:
        for url in urls:
            try:
                html = make_request(url)
                found_urls = parse_html(url, html)
            except requests.exceptions.RequestException:
                continue

            if found_urls:
                file.write("\n\n")
            for url in found_urls:
                file.write(url + "\n")


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"Total time elapsed: {elapsed:0.2F}s")
