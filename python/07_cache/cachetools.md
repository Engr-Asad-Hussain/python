## Cache Tools
This module provides various memoizing collections and decorators, including variants of the Python Standard Library `@lru_cache` function decorator.


## LRU cache implementation on specific function arguments
`@lru_cache` is limited when you want to include specific function arguments in the cache key builder. You can use open source library to control your cache key builder.

```py
from cachetools import cached, LRUCache
from cachetools.keys import hashkey
from uuid import UUID, uuid4

class bcolors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'


def logger(string: str):
    print(bcolors.GREEN + string + bcolors.ENDC)


@cached(
    cache=LRUCache(maxsize=128), 
    info=True,
    key=lambda id, *_: hashkey(id)
)
def get_user(id: UUID, status: str) -> str:
    logger('... Calculating hex')
    return id.hex

user1 = uuid4()
user2 = uuid4()
user3 = uuid4()
print(get_user(user1, "Active"))
print(get_user(user1, "Pending"))
print(get_user(user2, "Active"))
```

In this example the function `get_user` is called 3 times.
- First time it calls with "user1" and "Active" arguments. `cachetools` would use "id" as a cache key and function result as value.
- Second time it calls with "user1" and "Pending" arguments. Since "id" wouldn't change therefore result of a function is fetched from `cachetools`.
- Lastly, it calls with "user2" and "Active" arguments. In this case cache key "id" is changed, therefore it recalculate the function.

Hence as long as `id` is same the result of a function `get_user` is fetch from the cache.

## Reference
There are several features this library provides https://cachetools.readthedocs.io/en/latest/