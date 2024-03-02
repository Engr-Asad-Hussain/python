from fastapi import FastAPI

app = FastAPI()


# A "path" is also commonly called an "endpoint" or a "route".
# In OpenAPI, each of the HTTP methods is called an "operation".
# Following syntax is known as path decorator operation.
# Below the decorator is the path decorator function.
@app.get(path="/api")
async def root():
    return {"message": "Hello World Fast API!"}


@app.post(path="/api")
def generate_tokens():
    return {"message": "Generator Tokens"}


# You can see it directly at: http://127.0.0.1:8000/openapi.json
# You can see it directly at: http://127.0.0.1:8000/docs
# You can see it directly at: http://127.0.0.1:8000/redoc

# Reference: https://fastapi.tiangolo.com/tutorial/first-steps/
