"""
It contains an app/main.py file.
As it is inside a Python package (a directory with a file __init__.py), it is a "module" of
that package: app.main
Notes:
- And we can even declare global dependencies that will be combined with the dependencies for each APIRouter:
"""

from structure.dependencies import get_query_token, get_token_header
from structure.internal import admin
from structure.routers import items, users

from fastapi import Depends, FastAPI

app = FastAPI(dependencies=[Depends(get_query_token)])
app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    dependencies=[Depends(get_token_header)],
    tags=["Admin"],
    responses={401: {"description": "Unauthorized Operation"}},
)


@app.get(path="/health")
async def app_health():
    return {"message": "Service is up!"}
