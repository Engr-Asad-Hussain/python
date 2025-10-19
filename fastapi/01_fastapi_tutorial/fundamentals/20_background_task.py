from pydantic import EmailStr

from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def generate(email: str, message: str):
    with open("log.txt", mode="w") as file:
        content = f"Email sending to {email} ... Message: {message}"
        file.write(content)


@app.post(path="/api/send-email/{email}")
async def generate_email(email: EmailStr, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        generate, email, message="You have been invited to the newly created group."
    )
    return {"message": "Email will be generated asynchronously in background!"}


# Reference: https://fastapi.tiangolo.com/tutorial/background-tasks/
