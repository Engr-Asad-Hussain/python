import os
from typing import Annotated, Any

from pydantic import BaseModel, Field

from fastapi import Cookie, Depends, FastAPI, Header, HTTPException

app = FastAPI()


# In some cases you don't really need the return value of a dependency inside your path operation function.
# Or the dependency doesn't return a value.
# But you still need it to be executed/solved.
# For those cases, instead of declaring a path operation function parameter with Depends, you can add a list of dependencies to the path operation decorator.


class Items(BaseModel):
    title: str
    price: float = Field(ge=1)
    voting: int = Field(ge=0, le=5)


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "2201f3a515-02a6-4dc5-b1f9-e97964b91a78":
        raise HTTPException(
            status_code=401,
            detail={
                "message": "Please provide valid X-Token",
                "hint": "2201f3a515-02a6-4dc5-b1f9-e97964b91a78",
            },
        )


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "3201f3a515-02a6-4dc5-b1f9-e97964b91a78":
        raise HTTPException(
            status_code=401,
            detail={
                "message": "Please provide valid X-Key",
                "hint": "3201f3a515-02a6-4dc5-b1f9-e97964b91a78",
            },
        )


@app.get(
    path="/api/items",
    response_model=list[Items],
    status_code=200,
    dependencies=[Depends(verify_token), Depends(verify_key)],
)
async def item_list():
    rset = [
        {"title": "Dell Latitude", "price": 95000, "voting": 4},
        {"title": "Samsung A13", "price": 40000.0, "voting": 3},
        {"title": "Furniture", "price": 20000, "voting": 1},
    ]
    return [Items(**val) for val in rset]


# For debugging
@app.get(path="/app/pid")
async def app_process() -> dict[str, int]:
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-in-path-operation-decorators/
