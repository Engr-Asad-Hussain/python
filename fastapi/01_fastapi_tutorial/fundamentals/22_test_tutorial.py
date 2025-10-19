import os
from typing import Annotated

from fastapi.testclient import TestClient
from pydantic import BaseModel

from fastapi import FastAPI, Header, HTTPException

app = FastAPI()


@app.get(path="/")
async def read_root():
    return {"message": "This is an example of Fast API Tests."}


fake_x_token = "coneofsilence"
fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}


class Item(BaseModel):
    id: str
    title: str
    description: str | None = None


@app.get(path="/items/{item_id}", response_model=Item)
async def read_items(item_id: str, x_token: Annotated[str, Header()]):
    if x_token != fake_x_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token.")
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item does not exists.")
    return fake_db[item_id]


@app.post(path="/items", status_code=201, response_model=Item)
async def create_item(item: Item, x_token: Annotated[str, Header()]):
    if x_token != fake_x_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token.")
    if item.id in fake_db:
        raise HTTPException(status_code=409, detail="Item already exists.")
    fake_db[item.id] = item
    return item


# Ceveat
# In a real application, you probably would have your tests in a different file.
# And your FastAPI application might also be composed of several files/modules, etc.


client = TestClient(app)


def test_read_root():
    resp = client.get(url="/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "This is an example of Fast API Tests."}


def test_read_items():
    resp = client.get(url="/items/foo", headers={"X-Token": fake_x_token})
    assert resp.status_code == 200
    assert resp.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


def test_read_items_bad_token():
    resp = client.get(url="/items/foo", headers={"X-Token": fake_x_token + "gebbrish"})
    assert resp.status_code == 400
    assert resp.json() == {"detail": "Invalid X-Token."}


def test_read_inexistent_item():
    resp = client.get(url="/items/baz", headers={"X-Token": fake_x_token})
    assert resp.status_code == 404
    assert resp.json() == {"detail": "Item does not exists."}


def test_create_item():
    resp = client.post(
        url="/items",
        headers={"X-Token": fake_x_token},
        json={
            "id": "dip",
            "title": "Dipper",
            "description": "The dipper you go the better will be the result.",
        },
    )
    assert resp.status_code == 201
    assert resp.json() == {
        "id": "dip",
        "title": "Dipper",
        "description": "The dipper you go the better will be the result.",
    }


def test_create_item_bad_token():
    resp = client.post(
        url="/items",
        headers={"X-Token": fake_x_token + "gibbrish"},
        json={
            "id": "dip",
            "title": "Dipper",
            "description": "The dipper you go the better will be the result.",
        },
    )
    assert resp.status_code == 400
    assert resp.json() == {"detail": "Invalid X-Token."}


def test_create_existing_item():
    resp = client.post(
        url="/items",
        headers={"X-Token": fake_x_token},
        json={
            "id": "foo",
            "title": "Foo",
            "description": "There goes my hero",
        },
    )
    assert resp.status_code == 409
    assert resp.json() == {"detail": "Item already exists."}


# For debugging
@app.get(path="/app/pid")
async def app_process():
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/tutorial/testing/
