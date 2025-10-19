import os
from typing import Annotated

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()

# You can create dependencies that have sub-dependencies.
# They can be as deep as you need them to be.
# FastAPI will take care of solving them.


# It declares an optional query parameter q as a str, and then it just returns it.
async def query_extractor(q: str | None = None):
    return q


# Then you can create another dependency function (a "dependable") that at the same time
# declares a dependency of its own (so it is a "dependant" too):
async def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    item_cookie: Annotated[str | None, Cookie()] = None,
):
    return q if q else item_cookie


@app.get(path="/api/items")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
    return {
        "message": "Following are the provided query arguments.",
        "query_or_default": query_or_default,
    }


# For debugging
@app.get(path="/app/pid")
async def app_process() -> dict[str, int]:
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/
