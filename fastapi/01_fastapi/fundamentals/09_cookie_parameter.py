from fastapi import FastAPI, Cookie
from typing import Annotated


app = FastAPI()


# Define Cookie parameters the same way you define Query and Path parameters
# The cookie key would be the variable. Passed the cookie via headers.
@app.get("/api/store")
async def store(store_cookie: Annotated[str, Cookie()]):
    return {
        "message": "Following are the provided arguments.",
        "store_cookie": store_cookie,
    }


# Reference: https://fastapi.tiangolo.com/tutorial/cookie-params/
