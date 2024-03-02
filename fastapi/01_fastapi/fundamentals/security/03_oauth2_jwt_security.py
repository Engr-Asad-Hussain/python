import os
from datetime import datetime, timedelta, timezone
from typing import Annotated, Any, Callable
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr
from jose import JWTError, jwt
from passlib.context import CryptContext

# To get randomly generated password run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


fake_db = {
    "johndoe": {
        "username": "johndoe",
        "name": "john doe",
        "email": "johndoe@demo.io",
        "hashed_password": "$2b$12$1suqNPhtpa129H5hk8yNFehiW.hyNaFHDBY2uPNrjeeXybFzOGtr.",
        "disabled": True,
    },
    "alice": {
        "username": "alice",
        "name": "alice",
        "email": "alice@demo.io",
        "hashed_password": "$2b$12$B34pFjDU02jqQXjDJORU2eYQm2ELTlC5R7p6xk1rkb4M5m2G3GCaO",
        "disabled": False,
    },
}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI()


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class User(BaseModel):
    username: str
    name: str
    email: EmailStr
    disabled: bool


class UserDBIn(User):
    hashed_password: str


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


def get_user(db: dict[str, Any], uid: str) -> UserDBIn | None:
    if uid in db:
        user_dict = db[uid]
        return UserDBIn(**user_dict)


def create_access_token(data: dict[str, Any], expires_delta: int = 15):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)


def authenticate_user(db: dict[str, Any], username: str, password: str) -> UserDBIn:
    user = get_user(db, uid=username)
    if not user:
        raise HTTPException(status_code=400, detail="User not found.")
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Password mismatch.")
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    creds_exception: Callable[[str], HTTPException] = lambda x: HTTPException(
        status_code=401,
        detail=f"Invalid authentication credentials. {x}",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as e:
        raise creds_exception(str(e))
    else:
        user = get_user(fake_db, payload["sub"])
        if user is None:
            raise creds_exception("")
        return user


async def get_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled is True:
        raise HTTPException(status_code=422, detail="User is disabled.")
    return current_user


@app.post(path="/api/token", status_code=200)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = authenticate_user(fake_db, form_data.username, form_data.password)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return Token(access_token=access_token, token_type="Bearer")


@app.get(path="/api/users/me", status_code=200, response_model=User)
async def users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@app.get(path="/api/users/items", status_code=200)
async def users_items(current_user: Annotated[User, Depends(get_active_user)]):
    return {"owner": current_user.email}


# For debugging
@app.get(path="/app/pid")
async def app_process() -> dict[str, int]:
    return {"processPid": os.getpid()}


# Reference: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
