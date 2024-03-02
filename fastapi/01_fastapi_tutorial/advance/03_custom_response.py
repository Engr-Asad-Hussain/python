import os
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


# Performance:
# - `ORJSONResponse`: Significantly faster (often 6-10x) in JSON serialization compared to `JSONResponse`.
#                     This makes it ideal for performance-critical applications or those handling large amounts of data.
#                     Requires the external orjson library to be installed, as it leverages its optimized JSON serialization capabilities.
# - `JSONResponse`: Uses Python's built-in json module, which is relatively slow. It's suitable for
#                   basic scenarios where performance isn't a major concern.

app = FastAPI()
# app = FastAPI(default_response_class=ORJSONResponse)


# If you're returning Pydantic models, database objects, or custom classes, always let FastAPI do
# the serialization work for you. These data types might not always be directly serializable to JSON.


# You're sure your data is already JSON compatible: If the data you want to send back in your
# response is comprised of basic Python data types that are natively JSON serializable (strings,
# integers, floats, lists, dictionaries with string keys), then this data doesn't need further processing.
# Bypass `jsonable_encoder` for efficiency: Instead of relying on FastAPI's `jsonable_encoder` to check
# and prepare your data for serialization, you can directly pass your already JSON-safe data
# into the response class (e.g., `ORJSONResponse` or `JSONResponse`). This saves a bit of computational
# overhead because the encoder step is unnecessary.


"""
Example Block 1:
1. The function generates a Python dictionary ({"message": ..., "item_id": ...}).
2. FastAPI implicitly calls `jsonable_encoder` to ensure the dictionary is JSON-serializable.
3. The ORJSONResponse class receives the encoded dictionary and proceeds with serialization using orjson
"""


@app.get(path="/api/items/{item_id}", status_code=200, response_class=ORJSONResponse)
async def block_1(item_id: str):
    return {
        "message": "This is the OrJsonResponse.",
        "note": "This is passed to jsonable_encoder internally by Fast API despite having serializable return response i.e., dict.",
        "item_id": item_id,
    }


"""
Example Block 2:
1. The function directly creates an ORJSONResponse object with the dictionary as its content.
2. FastAPI doesn't need to engage `jsonable_encoder` because you've already explicitly provided a serializable dictionary.
3. The ORJSONResponse class immediately proceeds with serialization using orjson
"""


@app.get(
    path="/api/items/optimized/{item_id}",
    status_code=200,
    response_class=ORJSONResponse,
)
async def block_2(item_id: str):
    return ORJSONResponse(
        {
            "message": "This is the OrJsonResponse.",
            "note": "This bypass to jsonable_encoder because of having serializable return response i.e., dict.",
            "item_id": item_id,
        }
    )


"""
Conclustion
Performance Comparison:
- The second example is likely to be more performant because it avoids the additional step of 
  serializing the response content using `jsonable_encoder`. By directly passing the content to 
  ORJSONResponse, you reduce the overhead associated with the serialization process.

- However, the performance gain might be more noticeable for larger response payloads. For small 
  responses, the difference may not be significant. In practice, the performance improvement might 
  vary depending on the specific use case and the size of the data being returned.

- It's important to note that the choice between these approaches often involves trade-offs between 
  readability and performance. The first example is more concise and may be preferred for simplicity 
  unless the performance gain is crucial for your specific use case.
"""


# For debugging
@app.get(path="/app/pid")
async def app_process():
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/advanced/custom-response/
