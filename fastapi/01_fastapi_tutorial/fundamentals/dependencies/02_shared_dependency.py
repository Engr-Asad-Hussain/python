import os
from typing import Annotated, Any

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}


# When you need to use the common_parameters() dependency, you have to write the whole
# parameter with the type annotation and Depends()
# But because we are using Annotated, we can store that Annotated value in a variable
# and use it in multiple places:
commonsDep = Annotated[dict[str, Any], Depends(common_parameters)]


@app.get(path="/api/items")
async def read_items(commons: commonsDep):
    return commons


@app.get(path="/api/users")
async def read_users(commons: commonsDep):
    return commons


# For debugging
@app.get(path="/app/pid")
async def app_process() -> dict[str, int]:
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/tutorial/dependencies/
