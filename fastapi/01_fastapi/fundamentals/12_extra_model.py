from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


# Multiple models
class MUserIn(BaseModel):
    name: str
    email: EmailStr
    password: str


class MUserOut(BaseModel):
    name: str
    email: EmailStr


class MUserDB(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str


def fake_password_hasher(password: str) -> str:
    return "hashed:" + password


@app.post(path="/api/multiple-model/user", response_model=dict[str, str | MUserOut])
async def multiple_model(user: MUserIn):
    hashed_password = fake_password_hasher(user.password)
    user_in_db = MUserDB(**user.model_dump(), hashed_password=hashed_password)
    return {"message": "Following is the outcome.", "user": user_in_db}


# Reference: https://fastapi.tiangolo.com/tutorial/extra-models/
