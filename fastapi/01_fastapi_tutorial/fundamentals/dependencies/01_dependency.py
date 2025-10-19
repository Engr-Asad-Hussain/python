import os
from typing import Annotated, Any

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}


@app.get(path="/api/items")
async def read_items(commons: Annotated[dict[str, Any], Depends(common_parameters)]):
    return commons


@app.get(path="/api/users")
async def read_users(commons: Annotated[dict[str, Any], Depends(common_parameters)]):
    return commons


# For debugging
@app.get(path="/app/pid")
async def app_process() -> dict[str, int]:
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/tutorial/dependencies/
