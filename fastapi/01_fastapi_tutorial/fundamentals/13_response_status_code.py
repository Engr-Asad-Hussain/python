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


# The same way you can specify a response model, you can also declare the HTTP status code
# used for the response with the parameter status_code in any of the path operations:
# status_code can alternatively also receive an IntEnum, such as Python's http.HTTPStatus.
# You can use the convenience variables from fastapi.status
@app.post(
    path="/api/status-code/create",
    response_model=dict[str, str | MUserOut],
    status_code=201,
)
async def status_code_create(user: MUserIn):
    return {"message": "User successfully created!", "user": user}


# Reference: https://fastapi.tiangolo.com/tutorial/response-status-code/
