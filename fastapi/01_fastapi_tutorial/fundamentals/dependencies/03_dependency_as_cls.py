import os
from typing import Annotated, Any
from fastapi import FastAPI, Depends

app = FastAPI()


# The key factor is that a dependency should be a "callable".
class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 10) -> None:
        self.q = q
        self.skip = skip
        self.limit = limit


fake_database = [
    {"name": "Dependency"},
    {"name": "Injection"},
    {"name": "Classes"},
    {"name": "Function"},
]


@app.get(path="/api/items")
async def read_items(common: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    response: dict[str, Any] = {}
    if common.q is not None:
        response.update({"q": common.q})
    items = fake_database[common.skip : common.skip + common.limit]
    response.update({"items": items})
    return response


# But you see that we are having some code repetition here, writing CommonQueryParams twice:
# commons: Annotated[CommonQueryParams, Depends()]
@app.get(path="/api/topics")
async def read_topic(topic: Annotated[CommonQueryParams, Depends()]):
    return topic


# For debugging
@app.get(path="/app/pid")
async def app_process() -> dict[str, int]:
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/
