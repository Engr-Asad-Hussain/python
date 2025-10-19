import os
from enum import Enum

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, ValidationError

from fastapi import FastAPI

app = FastAPI()


class Dlevel(str, Enum):
    Basic = "Basic"
    Intermediate = "Intermediate"
    Difficult = "Difficult"
    Expert = "Expert"


fake_db = {
    "a52515e5-318e-4d15-9043-fea725ee92d0": {
        "title": "User Tutorial",
        "price": 299,
        "difficulty_level": Dlevel.Intermediate,
    },
    "426d2c30-27e4-464c-ab6d-52b5f0eaeedd": {
        "title": "Advance Tutorial",
        "price": 499,
        "difficulty_level": Dlevel.Difficult,
    },
    "f7320b46-dcac-4e51-a015-c26db3402027": {
        "title": "Experts Opinions",
        "price": 1499,
        "difficulty_level": Dlevel.Expert,
    },
}


class Item(BaseModel):
    title: str
    price: float
    difficulty_level: Dlevel


@app.post(path="/api/items/{item_id}", status_code=200)
async def upsert_item(item_id: str, item: Item | None = None):
    if item_id in fake_db:
        return fake_db[item_id]
    else:
        if item is None:
            raise HTTPException(
                status_code=400, detail="Please provide body arguments."
            )
        try:
            data = Item.model_validate(item)
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=e.errors())
        else:
            # When you return a Response, FastAPI will pass it directly.
            # It won't do any data conversion with Pydantic models, it won't convert the contents to
            # any type, etc.
            # This gives you a lot of flexibility. You can return any data type, override any
            # data declaration or validation, etc.
            # But if you return a Response directly, the data won't be automatically converted, and
            # the documentation won't be automatically generated (for example, including the specific
            # "media type", in the HTTP header Content-Type as part of the generated OpenAPI).
            return JSONResponse(content=jsonable_encoder(data), status_code=201)


@app.get(path="/legacy")
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")


# For debugging
@app.get(path="/app/pid")
async def app_process():
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/advanced/additional-status-codes/
# Reference: https://fastapi.tiangolo.com/advanced/response-directly/
