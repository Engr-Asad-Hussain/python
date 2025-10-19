import os

from fastapi.responses import JSONResponse, Response

from fastapi import FastAPI

app = FastAPI()


@app.post(path="/api/login")
async def login(response: Response):
    response.set_cookie(
        key="refresh_token",
        value="426d2c30-27e4-464c-ab6d-52b5f0eaeedd",
        httponly=True,
        samesite="none",
        expires=300,
    )
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
    response.set_cookie(
        key="refresh_token",
        value="426d2c30-27e4-464c-ab6d-52b5f0eaeedd",
        httponly=True,
        samesite="none",
        expires=300,
    )
    return response


# For debugging
@app.get(path="/app/pid")
async def app_process():
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/advanced/response-cookies/
