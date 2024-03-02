from typing import Any, Callable
from flask import request


def parse_header(fn: Callable[..., Any]):
    """
    - Inject the `async_mode` keyward to the view function based on the
      incoming header i.e., Async-Mode
    - The view function will be receiving an additional keyward argument as `async_mode`
      that can be used to further in processing request.
    """

    def wrapper(*args: Any, **kwargs: dict[str, Any]) -> Callable[..., Any]:
        async_mode = request.headers.get("Async-Mode", "false")
        kwargs["async_mode"] = async_mode.lower() == "true"
        return fn(*args, **kwargs)

    return wrapper
