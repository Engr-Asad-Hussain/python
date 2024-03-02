from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Declare your data model as a class that inherits from BaseModel.
# This is for the request body parameters
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 0.13


@app.post(path="/api/items")
async def create_items(item: Item):
    total = item.price + (item.price * item.tax)
    resp_body: dict[str, Any] = {**item.model_dump(), "total": total}
    return {"message": "Following is your provided data.", "item": resp_body}


# The function parameters will be recognized as follows:
# 1. If the parameter is also declared in the path, it will be used as a path parameter.
# 2. If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
# 3. If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.
@app.put(path="/api/items/{item_id}")
async def update_item(
    item_id: int, item: Item, q: str | None = None, skip: int = 0, limit: int = 10
):
    return {
        "message": "Following is your provided path parameter and request body.",
        "item": item,
        "id": item_id,
        "query": {"q": q, "skip": skip, "limit": limit},
    }


# Reference: https://fastapi.tiangolo.com/tutorial/body/
