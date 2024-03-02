from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()


# There are some cases where you might need to convert a data type (like a Pydantic model) to
# something compatible with JSON (like a dict, list, etc).
# For example, if you need to store it in a database.
# For that, FastAPI provides a jsonable_encoder() function.
class JsonEncoder(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


@app.put(path="/api/json/encoder")
async def json_encoder(json_encoder: JsonEncoder):
    json_encoder_dict = jsonable_encoder(json_encoder)
    print(json_encoder_dict)
    print(type(json_encoder_dict))
    return {
        "message": "Json Encoder",
        "json_encoder": json_encoder,
        "type": f"This is the type of jsonable_encoder: {type(json_encoder_dict)}",
    }


# Reference: https://fastapi.tiangolo.com/tutorial/encoder/
