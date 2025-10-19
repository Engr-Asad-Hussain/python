from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=("http://localhost:3000", "http://localhost:3001"),
    allow_methods=("*",),  # Default GET
    allow_headers=("*",),  # Default ()
    allow_credentials=True,  # Default False
    max_age=600,  # Sets a maximum time in seconds for browsers to cache CORS responses.
)


@app.get(path="/api/items")
async def items():
    return {"message": "Items are protected!"}
