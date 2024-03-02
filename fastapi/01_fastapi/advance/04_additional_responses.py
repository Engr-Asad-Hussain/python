import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    id: str
    is_valid: bool


class Message(BaseModel):
    detail: str


@app.get(
    path="/api/items/{item_id}",
    response_model=Item,
    responses={
        200: {"content": {"plain/txt": {}}},
        404: {"model": Message, "description": "Not Found"},
    },
    # default responses: 200, 422 (pydantic validation)
)
async def read_item(item_id: str):
    if item_id == "f7320b46-dcac-4e51-a015-c26db3402028":
        raise HTTPException(status_code=404, detail="Item does not exists.")

    if item_id == "f7320b46-dcac-4e51-a015-c26db3402029":
        return PlainTextResponse(content="This is the plain response.")

    return Item(id="f7320b46-dcac-4e51-a015-c26db3402027", is_valid=True)


# responses = {
#     404: {"description": "Item not found"},
#     302: {"description": "The item was moved"},
#     403: {"description": "Not enough privileges"},
# }
# @app.get(responses={**responses, 401: {"description": "Unauthorized"}})


# For debugging
@app.get(path="/app/pid")
async def app_process():
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/advanced/additional-responses/
