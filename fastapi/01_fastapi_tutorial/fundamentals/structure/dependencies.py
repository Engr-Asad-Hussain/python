"""
There's also an app/dependencies.py file, just like app/main.py, it is a "module": app.dependencies
"""

from typing import Annotated

from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake_checker":
        raise HTTPException(
            status_code=400, detail="Please provider valid X-Token header."
        )


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(
            status_code=400, detail="Please provide valid jessica token."
        )
