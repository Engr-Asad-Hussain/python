## Cache using @lru_cache
This section contains how to use `@lru_cache`


## Content
- [Implementing a cache using a Python Dictionary](#implementing-a-cache-using-a-python-dictionary)
- [Caching strategies](#caching-strategies)
- [Diving into the Least Recently Used (LRU) cache strategy](#diving-into-the-least-recently-used-lru-cache-strategy)
- [Using @lru_cache to implement an LRU cache](#using-lru_cache-to-implement-an-lru-cache-in-python)
- [Example of @lru_cache](#minimal-example-of-lru_cache)
- [Unpacking the functionality of @lru_cache](#unpacking-the-functionality-of-lru_cache)
- [Evicting cache entries based on both time and space](#evicting-cache-entries-based-on-both-time-and-space)
- [Caculating memory size of @lru_cache](#caculating-the-memory-size-of-lru_cache)
- [Reference](#reference)

## Implementing a Cache Using a Python Dictionary
You can implement a caching solution in Python using a dictionary.
```py
import code
import requests


cache = dict()


def get_article_from_server(url: str) -> str:
    print('Fetching article')
    resp = requests.get(url)
    return resp.text

def get_article(url: str):
    print('Getting article ...')
    if url in cache:
        return cache[url]
    else:
        result = get_article_from_server(url)
        cache[url] = result
        return result

get_article('https://realpython.com/sorting-algorithms-python/')
get_article('https://realpython.com/sorting-algorithms-python/')
```
Notice how you get the string "Fetching article from server..." printed a single time despite calling `get_article()` twice. This happens because, after accessing the article for the first time, you put its URL and content in the cache dictionary. The second time, the code doesn’t need to fetch the item from the server again.


## Caching Strategies
There’s one big problem with this cache implementation using dictionary: the content of the dictionary will grow indefinitely! As the user downloads more articles, the application will keep storing them in memory, eventually causing the application to crash.

To work around this issue, you need a strategy to decide which articles should stay in memory and which should be removed. These caching strategies are algorithms that focus on managing the cached information and choosing which items to discard to make room for new ones.

There are several different strategies that you can use to evict items from the cache and keep it from growing past from its maximum size. Here are five of the most popular ones, with an explanation of when each is most useful:
| Strategy | Eviction policy | Use case |
| -------- | -------- | ---------- |
| `First-In/First-Out (FIFO)` | Evicts the oldest of the entries | Newer entries are most likely to be reused |
| `Last-In/First-Out (LIFO)` | Evicts the latest of the entries | Older entries are most likely to be reused |
| `Least Recently Used (LRU)` | Evicts the least recently used entry | Recently used entries are most likely to be reused |
| `Most Recently Used (MRU)` | Evicts the most recently used entry | Least recently used entries are most likely to be reused |
| `Least Frequently Used (LFU)` | Evicts the least often accessed entry | Entries with a lot of hits are more likely to be reused |

In the sections below, you’ll take a closer look at the LRU strategy and how to implement it using the `@lru_cache` decorator from Python’s functools module.


## Diving Into the Least Recently Used (LRU) Cache Strategy
A cache implemented using the `LRU` strategy organizes its items in order of use. Every time you access an entry, the LRU algorithm will move it to the top of the cache. This way, the algorithm can quickly identify the entry that’s gone unused the longest by looking at the bottom of the list.


## Using @lru_cache to Implement an LRU Cache in Python
Just like the caching solution you implemented earlier, `@lru_cache` uses a dictionary behind the scenes. It caches the function’s result under a key that consists of the call to the function, including the supplied arguments. This is important because it means that these arguments have to be hashable for the decorator to work.


## Minimal example of @lru_cache
```py
from functools import lru_cache
import requests


@lru_cache
def get_article_from_server(url: str) -> str:
    print('Fetching article')
    resp = requests.get(url)
    return resp.text

get_article_from_server('https://realpython.com/sorting-algorithms-python/')
get_article_from_server('https://realpython.com/sorting-algorithms-python/')
```


## Unpacking the Functionality of @lru_cache
With the `@lru_cache` decorator in place, you store every call and answer in memory to access later if requested again. But how many calls can you save before running out of memory?

Python’s @lru_cache decorator offers a `maxsize` attribute that defines the maximum number of entries before the cache starts evicting old items. By default, maxsize is set to 128. If you set maxsize to None, then the cache will grow indefinitely, and no entries will be ever evicted. This could become a problem if you’re storing a large number of different calls in memory.
```py
from functools import lru_cache
import requests


@lru_cache(maxsize=16)
def get_article_from_server(url: str) -> str:
    print('Fetching article')
    resp = requests.get(url)
    return resp.text

get_article_from_server('https://realpython.com/sorting-algorithms-python/')
get_article_from_server('https://realpython.com/sorting-algorithms-python/')
get_article_from_server('https://realpython.com/sorting-algorithms-python/')
get_article_from_server('https://realpython.com/sorting-algorithms-python/')
```

In this case, you’re limiting the cache to a maximum of 16 entries. When a new call comes in, the decorator’s implementation will evict the least recently used of the existing 16 entries to make a place for the new item.

To see what happens with this new addition to the code, you can use `cache_info()`, provided by the @lru_cache decorator, to inspect the number of hits and misses and the current size of the cache. For clarity, remove the code that times the runtime of the function.

```py
print(get_article_from_server.cache_info())
```

Here’s a breakdown of the properties provided by cache_info():
- `hits=52` is the number of calls that @lru_cache returned directly from memory because they existed in the cache.
- `misses=30` is the number of calls that didn’t come from memory and were computed. Since you’re trying to find the number of steps to reach the thirtieth stair, it makes sense that each of these calls missed the cache the first time they were made.
- `maxsize=16` is the size of the cache as you defined it with the maxsize attribute of the decorator.
- `currsize=16` is the current size of the cache. 


## Evicting Cache Entries Based on Both Time and Space
The `@lru_cache` decorator evicts existing entries only when there’s no more space to store new listings. With sufficient space, entries in the cache will live forever and never get refreshed.

You can implement this idea into a new decorator that extends @lru_cache. If the caller tries to access an item that’s past its lifetime, then the cache won’t return its content, forcing the caller to fetch the article from the network.
```py
from datetime import datetime, timedelta, timezone
from functools import lru_cache, wraps


def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.now(tz=timezone.utc) + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.now(tz=timezone.utc) >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.now(tz=timezone.utc) + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache

@timed_lru_cache(1)
def get_article_from_server(url: str) -> str:
    print('Fetching article')
    resp = requests.get(url)
    return resp.text

get_article_from_server('https://realpython.com/sorting-algorithms-python/')
get_article_from_server('https://realpython.com/sorting-algorithms-python/')
get_article_from_server('https://realpython.com/sorting-algorithms-python/')
get_article_from_server('https://realpython.com/sorting-algorithms-python/')
get_article_from_server('https://realpython.com/sorting-algorithms-python/')
```


## Caculating the memory size of @lru_cache
```py
import sys
from functools import lru_cache
import requests

maxsize = 10
@lru_cache(maxsize=maxsize)
def get_address(ip: str) -> dict[str, str]:
    # This function returns a dictionary containing a keys country, regionName and city
    resp = requests.get(f"http://ip-api.com/json/{ip}", params={"fields": "country,regionName,city"})
    return resp.json()
```

- Steps to Estimate Memory Usage. 
- Measure the Size of Cached Items:
  - Use Python's `sys.getsizeof()` function to measure the size of each cached entry.
  - Since `lru_cache` stores both the function arguments and return values, you need to measure the size of:
    - The input argument (ip: str).
  - The output value (dictionary containing country, regionName, and city).
  - Compute Total Cache Size:
- Multiply the size of one cached entry by maxsize to estimate the total memory used by the cache.
- Benchmark for Accuracy:
  - Use real or representative input data for the ip values to get an accurate estimate of memory usage.

```py
def measure_cache_entry(ip: str):
    result = get_address(ip)
    ip_size = sys.getsizeof(ip)
    result_size = sys.getsizeof(result) + sum(sys.getsizeof(v) for v in result.values())
    entry_size = ip_size + result_size
    return entry_size
entry_size = measure_cache_entry('43.246.221.3')
print(f"Memory used per entry: {entry_size} bytes")
print(f"Estimated total memory usage for maxsize={maxsize}: {entry_size * maxsize} bytes")
```

- Why Calculate the Size of result and Its Values?
- When you use `sys.getsizeof(result)`, it gives you the size of the dictionary object itself, but it doesn't include the sizes of the values stored inside the dictionary. In Python, `sys.getsizeof()` only measures the memory footprint of the container object (like a dictionary or a list) and not the objects it contains.

```python
import sys

data = {"key1": "value1", "key2": "value2"}

print(sys.getsizeof(data))  # Size of the dictionary object itself
print(sys.getsizeof(data["key1"]))  # Size of the string "value1"
```
- The size of the dictionary (sys.getsizeof(data)) includes metadata, like the hash table and pointers to the keys/values.
- The sizes of the individual values (sys.getsizeof(data["key1"]), etc.) are not included in the size of the dictionary.
- Key Takeaways
  - Always use `sys.getsizeof()` on the keys and values of a dictionary to get an accurate memory estimate.
  - The dictionary’s sys.getsizeof() gives the size of the container but not the contents.
  - The proper total size of a dictionary is: `total_size = sys.getsizeof(d) + sum(sys.getsizeof(k) for k in d.keys()) + sum(sys.getsizeof(v) for v in d.values())`


## Reference
- https://realpython.com/lru-cache-python/