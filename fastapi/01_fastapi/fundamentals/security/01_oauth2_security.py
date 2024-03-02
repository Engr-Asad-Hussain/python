import os
from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    disabled: bool = False
    token: str


def fake_decode_token(token: str) -> User:
    # Validate Token
    return User(
        name="Asad Hussain",
        email="asad.h1998@yahoo.com",
        password="password123@",
        disabled=False,
        token=token,
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    return fake_decode_token(token)


@app.get(
    path="/api/users/me",
    status_code=200,
    response_model=User,
    summary="Get the information of current user.",
)
async def users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@app.get(path="/api/items")
async def get_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


# For debugging
@app.get(path="/app/pid")
async def app_process() -> dict[str, int]:
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/tutorial/security/get-current-user/
