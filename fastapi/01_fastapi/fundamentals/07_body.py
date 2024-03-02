from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field, HttpUrl
from typing import Annotated

app = FastAPI()


# Declare multiple body parameters, e.g. cloth, user and singular key-value:
# You can add multiple body parameters to your path operation function, even though a request can only have a single body.
class CategoryModel(BaseModel):
    title: str
    description: str


class UserModel(BaseModel):
    name: str
    username: str
    password: str


class DisplayModel(BaseModel):
    inches: str


@app.put(path="/api/cloths/{cloth_id}")
async def update_category(
    cloth_id: Annotated[int, Path(title="Cloth Id")],
    cloth: CategoryModel,
    user: UserModel,
    display: Annotated[DisplayModel, Body(embed=True)],
    is_important: Annotated[bool, Body()],
    q: Annotated[str | None, Query(title="Search parameter")] = None,
):
    return {
        "message": "Following is the provided arguments.",
        "clothId": cloth_id,
        "body": {
            "cloth": cloth,
            "user": user,
            "isImportant": is_important,
            "display": display,
        },
        "q": q,
    }


# Declare validation and metadata inside of Pydantic models using Pydantic's Field.
# Declare deeply nested JSON "objects" with specific attribute names, types and validations.
# Apart from normal singular types like str, int, float, etc. you can use more complex singular types that inherit from str.
# Pydantic's HttpUrl instead of a str:
class ReviewsModel(BaseModel):
    name: str
    email: str
    profile: HttpUrl


class BookModel(BaseModel):
    title: str = Field(title="Name of a book", max_length=20)
    author: str
    price: float
    quantity: int = Field(description="Number of books ordered", ge=1)
    seller: list[str]
    tags: set[str]  # remove duplicates
    reviews: ReviewsModel
    comments: list[ReviewsModel]


@app.post(path="/api/books")
async def create_books(book: BookModel):
    return {"message": "Following are the books", "books": book}


# You can declare examples for a Pydantic model that will be added to the generated JSON Schema.
class StoreModel(BaseModel):
    title: str = Field(title="Title of the store", max_length=150)
    location: str = Field(
        title="Location of the store",
        max_length=150,
        examples=["The metadata for the generated docs/redoc."],
    )
    is_approved: bool = False

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Al-Rehman General Store",
                    "location": "Karachi, Pakistan",
                    "is_approved": True,
                },
                {
                    "title": "Chief Center",
                    "location": "Lahore, Pakistan",
                },
            ]
        }
    }


@app.post(path="/api/store")
async def create_store(
    store: Annotated[
        StoreModel,
        Body(
            example=[
                {
                    "title": "Al-Rehman General Store",
                    "location": "Karachi, Pakistan",
                    "is_approved": True,
                }
            ],
            openapi_examples={
                "normal": {
                    "summary": "Short description of the example",
                    "description": "A longer description",
                    "value": {
                        "title": "Al_rehman General Store",
                        "location": "Karachi, Pakistan",
                        "is_approved": True,
                    },
                },
                "invalid": {
                    "summary": "Short description of the example",
                    "description": "A longer description",
                    "value": {
                        "title": 200,
                        "location": ["Pakistan", "United Kingdom"],
                        "is_approved": "String value",
                    },
                },
            },
        ),
    ]
):
    return {"message": "Following are the stores.", "store": store}


# Reference: https://fastapi.tiangolo.com/tutorial/body-multiple-params/
# Reference: https://fastapi.tiangolo.com/tutorial/body-fields/
# Reference: https://fastapi.tiangolo.com/tutorial/body-nested-models/
# Reference: https://fastapi.tiangolo.com/tutorial/schema-extra-example/
