from fastapi import FastAPI, Path
from fastapi.responses import RedirectResponse, JSONResponse
from typing import Annotated, Any
from pydantic import EmailStr, BaseModel, Field
from datetime import datetime

app = FastAPI()


# You can declare the type used for the response by annotating the path operation function return type.
# Model Response - Return Type
# Validate the returned data.
# It will limit and filter the output data to what is defined in the return type.
# If you declare both a return type and a response_model, the response_model will take priority and be used by FastAPI.
class Mobile(BaseModel):
    title: str
    price: float
    email: EmailStr


@app.get(path="/api/mobiles")
async def mobiles() -> Mobile:
    return Mobile(title="Samsung A13", price=29000, email="demo@mobile.io")


@app.get(path="/api/mobile/list")
async def mobiles_list() -> list[Mobile]:
    return [
        Mobile(title="Samsung A13", price=29000, email="demo@mobile.io"),
        Mobile(title="Infinix Zero 3", price=20000, email="demo@mobile.io"),
    ]


@app.get(path="/api/response-model", response_model=Mobile)
async def response_model() -> Any:
    return Mobile(title="Samsung A13", price=29000, email="demo@mobile.io")


# FastAPI will take care of filtering out all the data that is not declared in the output model (using Pydantic).
class UserIn(BaseModel):
    name: str = Field(max_length=150)
    username: EmailStr
    password: str = Field(max_length=150)


class UserOut(BaseModel):
    name: str = Field(max_length=150)
    username: EmailStr


@app.post(path="/api/users", response_model=UserOut)
async def create_users(user: UserIn) -> Any:
    return user


# We can use classes and inheritance to take advantage of function type annotations to get better
# support in the editor and tools, and still get the FastAPI data filtering.
class BaseUser(BaseModel):
    name: str = Field(max_length=150)
    username: EmailStr


class UserInn(BaseUser):
    password: str


@app.post(path="/api/base/users")
async def base_users(user: UserInn) -> BaseUser:
    return user


# Other Return Type Annotations
@app.get(path="/api/token")
async def api_token(teleport: bool = False):
    if teleport is True:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        return JSONResponse(
            content={"message": "Following is the response"}, status_code=201
        )


# You can set the path operation decorator parameter response_model_exclude_unset=True
# to omit default values in the response
class Token(BaseModel):
    value: str
    generated_at: datetime = datetime.utcnow()
    author: str = "Global Admin"


token_list = [
    Token(value="2201f3a515-02a6-4dc5-b1f9-e97964b91a78", author="OA"),
    Token(value="2201f3a515-02a6-4dc5-b1f9-e97964b91a78", author="RO"),
]


@app.get(
    path="/api/get-token/{token_id}",
    response_model=Token,
    response_model_exclude_unset=True,
    response_model_include={"value"},
)
async def get_token(token_id: Annotated[int, Path(ge=0, le=1)]):
    return token_list[token_id]


# Reference: https://fastapi.tiangolo.com/tutorial/response-model/
