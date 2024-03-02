from fastapi import FastAPI, Header
from typing import Annotated

app = FastAPI()


# Define Header parameters the same way you define Query, Path and Cookie parameters.
# HTTP headers are case-insensitive, so, you can declare them with standard Python style (also known as "snake_case").
@app.get("/api/headers")
async def store_headers(
    x_token: Annotated[list[str], Header()],
    user_agent: Annotated[str | None, Header(convert_underscores=True)] = None,
):
    return {
        "message": "Following are the headers",
        "user_agent": user_agent,
        "x_token": x_token,
    }


# Reference: https://fastapi.tiangolo.com/tutorial/header-params/
