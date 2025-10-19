from typing import Annotated, Any

from fastapi import FastAPI, File, Form, Header, UploadFile, status

app = FastAPI()


# Form Data
@app.post(
    path="/api/form/create",
    status_code=status.HTTP_201_CREATED,
    response_model=dict[str, str | Any],
)
async def form_create(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    content_type: Annotated[str, Header()],
):
    return {
        "message": "Form data has been accepted",
        "username": username,
        "password": password,
        "header": {
            "info": "Data from forms is normally encoded using the 'media type': 'application/x-www-form-urlencoded'.",
            "content_type": content_type,
        },
    }


# Request Files
@app.post(path="/api/files")
async def send_files(file: Annotated[bytes, File()]):
    return {"message": "We have received the files"}


@app.post(path="/api/uploadfile")
async def upload_file(token: Annotated[str, Form()], file: UploadFile | None = None):
    if file is None:
        return {"file": "Please provide file", "token": token}
    else:
        return {"file": file.filename, "token": token}


# Reference: https://fastapi.tiangolo.com/tutorial/request-forms/
# Reference: https://fastapi.tiangolo.com/tutorial/request-files/
# Reference: https://fastapi.tiangolo.com/tutorial/request-forms-and-files/
