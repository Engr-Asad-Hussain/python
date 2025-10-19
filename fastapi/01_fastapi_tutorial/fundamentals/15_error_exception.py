from fastapi.exception_handlers import http_exception_handler
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHttpException

from fastapi import FastAPI

app = FastAPI()


# Use HTTPException
# To return HTTP responses with errors to the client you use HTTPException
@app.get(path="/api/http/{http_id}")
async def specific_http(http_id: int):
    if http_id not in (200, 201):
        raise HTTPException(
            # status_code=400, detail="Please provide valid http code in (200, 201)"
            status_code=400,
            detail={"message": "Please provide valid http code in (200, 201)"},
            headers={"X-Token": "Please enter x-token as an header."},
        )
    return {"message": "Request accepted"}


# Custom Exceptions
class BadRequest(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


@app.exception_handler(BadRequest)
async def badrequest_exception_handler(request: Request, exc: BadRequest):
    return JSONResponse(status_code=400, content={"message": exc.name})


@app.get(path="/api/exception/{exception_id}")
async def specific_exception(exception_id: int):
    raise BadRequest(f"This is not a valid Exception({exception_id}).")


# Override default exceptions
@app.exception_handler(RequestValidationError)
async def request_validation_error(request: Request, exc: RequestValidationError):
    return PlainTextResponse(content=str(exc), status_code=400)


@app.exception_handler(StarletteHttpException)
async def custom_http_exception_handler(request: Request, exc: StarletteHttpException):
    print("Hit Internal Exception")
    return await http_exception_handler(request, exc)


# Reference: https://fastapi.tiangolo.com/tutorial/handling-errors/
