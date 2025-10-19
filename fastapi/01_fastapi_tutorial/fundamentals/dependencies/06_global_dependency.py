import os
from typing import Annotated

from pydantic import BaseModel, Field

from fastapi import Depends, FastAPI, Header, HTTPException

# For some types of applications you might want to add dependencies to the whole application.


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


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get(
    path="/api/items",
    response_model=list[Items],
    status_code=200,
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


# Reference: https://fastapi.tiangolo.com/tutorial/dependencies/global-dependencies/
