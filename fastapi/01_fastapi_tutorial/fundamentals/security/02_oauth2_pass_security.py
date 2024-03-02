import os
from typing import Annotated, Any
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr


app = FastAPI()

fake_db = {
    "johndoe": {
        "username": "johndoe",
        "name": "john doe",
        "email": "johndoe@demo.io",
        "hashed_password": "fake-hash-password",
        "disabled": True,
    },
    "alice": {
        "username": "alice",
        "name": "alice",
        "email": "alice@demo.io",
        "hashed_password": "fake-hash-password",
        "disabled": False,
    },
}


def fake_hasher(password: str) -> str:
    return "fake-hash-password"


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")


class User(BaseModel):
    username: str
    name: str
    email: EmailStr
    disabled: bool


class UserDBIn(User):
    hashed_password: str


def get_user(db: dict[str, Any], uid: str):
    if uid in db:
        user_dict = db[uid]
        return UserDBIn(**user_dict)


def fake_decode_token(token: str):
    return get_user(fake_db, uid=token)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=422, detail="User is disabled.")
    return current_user


@app.get(
    path="/api/users/me",
    status_code=200,
)
async def users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@app.post(path="/api/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="User not found.")
    user = UserDBIn(**user_dict)
    hashed_password = fake_hasher(form_data.password)
    if not (hashed_password == user.hashed_password):
        raise HTTPException(status_code=400, detail="Password is incorrect.")

    return {"access_token": user.username, "token_type": "bearer"}


# For debugging
@app.get(path="/app/pid")
async def app_process() -> dict[str, int]:
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
