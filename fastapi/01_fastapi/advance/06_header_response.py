import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response

app = FastAPI()


@app.post(path="/api/login")
async def login(response: Response):
    response.headers["X-Session"] = "426d2c30-27e4-464c-ab6d-52b5f0eaeedd"
    return {"access_token": "f7320b46-dcac-4e51-a015-c26db3402027"}


# - Keep in mind that if you return a response directly instead of using the Response parameter,
#   FastAPI will return it directly.
# - So, you will have to make sure your data is of the correct type. E.g. it is compatible
#   with JSON, if you are returning a JSONResponse.
# - And also that you are not sending any data that should have been filtered by a response_model
@app.post(path="/api/fake-login")
async def fake_login():
    content = {"access_token": "f7320b46-dcac-4e51-a015-c26db3402027"}
    response = JSONResponse(content)
    response.headers["X-Session"] = "426d2c30-27e4-464c-ab6d-52b5f0eaeedd"
    response.headers["Content-Language"] = "en-PK"
    return response
    # Keep in mind that custom proprietary headers can be added using the 'X-' prefix.


# For debugging
@app.get(path="/app/pid")
async def app_process():
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/advanced/response-headers/
