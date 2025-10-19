from functools import wraps
from typing import Any, Callable, List, Tuple

type IRegistry = List[Tuple[str, str, Callable[..., None]]]
_registry: IRegistry = []


def register_command(group: str, name: str):
    def decorator(func: Callable[..., None]):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            return func(*args, **kwargs)

        _registry.append((group, name, wrapper))
        return wrapper

    return decorator


def get_registry() -> IRegistry:
    # This is an helper function simply returns a copy of the registry
    # we can work with it locally without acidently removing the items present
    # in the registry.
    return _registry.copy()
