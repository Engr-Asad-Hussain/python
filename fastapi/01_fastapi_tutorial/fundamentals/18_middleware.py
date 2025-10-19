import time
from typing import Any, Callable

from fastapi.requests import Request

from fastapi import FastAPI

app = FastAPI()

# Before and after the response¶
# You can add code to be run with the request, before any path operation receives it.
# And also after the response is generated, before returning it.


@app.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable[..., Any]):
    print("Starting middleware")
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print("Returning response for middleware")
    return response


@app.get(path="/api/items")
async def items():
    print("Starting path operation function ...")
    return {"message": "Items has been rejected."}
