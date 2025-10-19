import os

import yaml
from fastapi.requests import Request
from pydantic import BaseModel, ValidationError

from fastapi import FastAPI, HTTPException

app = FastAPI()


def magic_validator(raw_body: bytes):
    return {
        "size": len(raw_body),
        "content": {
            "name": "Maagician",
            "description": "Just kiddin, no magic ✨",
            "price": 99.0,
        },
    }


@app.post(
    path="/api/items",
    openapi_extra={
        "requestBody": {
            "content": {
                "application/json": {
                    "schema": {
                        "required": ["name", "description"],
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "description": {"type": "string"},
                            "price": {"type": "number"},
                        },
                    }
                },
            },
            "required": True,
        }
    },
)
async def create_item(request: Request):
    raw_body = await request.body()
    return magic_validator(raw_body)


class YamlContent(BaseModel):
    name: str
    tags: list[str]


@app.post(path="/api/yaml-content")
async def yaml_content(request: Request):
    raw_body = await request.body()
    try:
        data = yaml.safe_load(raw_body)
    except yaml.YAMLError:
        raise HTTPException(status_code=400, detail="Invalid Yaml.")

    try:
        content = YamlContent.model_validate(data)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())
    else:
        return content


# For debugging
@app.get(path="/app/pid")
async def app_process():
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/
