from fastapi import FastAPI

app = FastAPI(
    title="API Documentation",
    summary="This is the tutorial examples provided in official documentation.",
    description="""
    ## Getting started with Fast API.
    ## Content
    - Items
    - Users
    - Dependencies and much more ...
    """,
    version="0.0.1",
    terms_of_service="https://learning.info/docs",
    contact={
        "name": "Asad Hussain",
        "email": "demonstrator@debug.io",
        "url": "https://demonstrator.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        "identifier": "MIT",
    },
    openapi_tags=[
        {
            "name": "Users",
            "description": "Operations with users. The **login** logic is also here.",
        },
        {
            "name": "Items",
            "description": "Manage items. So _fancy_ they have their own docs.",
            "externalDocs": {
                "description": "Items external docs",
                "url": "https://fastapi.tiangolo.com/",
            },
        },
    ],
    openapi_url="/api/openapi.json",
    # If you want to disable the OpenAPI schema completely you can set openapi_url=None
    docs_url="/api/docs",
    # You can disable it by setting docs_url=None.
    redoc_url="/api/redocs",
    # You can disable it by setting redoc_url=None
)


@app.get(path="/items/", tags=["Items"])
async def read_items():
    return [{"name": "Katana"}]


@app.get("/users/", tags=["Users"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]


# Reference: https://fastapi.tiangolo.com/tutorial/metadata/
