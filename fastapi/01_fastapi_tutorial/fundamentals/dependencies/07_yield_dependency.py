import os
from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException


# FastAPI supports dependencies that do some extra steps after finishing.
# Exit code, cleanup code, teardown code, closing code or context manager.

app = FastAPI()


class DBSession:
    def __init__(self) -> None:
        self.conn = None

    async def create(self) -> None:
        import asyncio

        await asyncio.sleep(3)
        print("Creating database connection...")

    def close(self) -> None:
        print("Closing database connection...")


class DBExceptions(Exception):
    pass


async def get_db():
    """
    - The code following the yield statement is executed after the response has been delivered.
    - You can look for that specific exception inside the dependency with except SomeException.
    - FastAPI uses Context Manager internally to achieve this.
    """
    print("Starting get_db")
    db = DBSession()
    try:
        conn = await db.create()
        yield conn
    except DBExceptions:
        raise HTTPException(
            status_code=500, detail="Something went wrong with database"
        )
    finally:
        db.close()


@app.get(path="/api/items")
async def get_items(db: Annotated[DBSession, Depends(get_db)]):
    print("Starting get_items")
    print(f"Database instance: {db}")
    return {"message": "Successfully fetched items from database."}


# For debugging
@app.get(path="/app/pid")
async def app_process() -> dict[str, int]:
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
