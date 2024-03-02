from enum import Enum
from fastapi import FastAPI

app = FastAPI()


# When you declare other function parameters that are not part of the path parameters,
# they are automatically interpreted as "query" parameters.
db = ({"name": "Samsung"}, {"name": "Telenore"}, {"name": "Jazz"})


class QueryEnum(str, Enum):
    health = "health"
    education = "education"
    sports = "sports"


@app.get(path="/api/items")
def items(
    skip: int,
    limit: int = 10,
    q: str | None = None,
    category: QueryEnum = QueryEnum.health,
):
    if q is not None:
        return {"message": f"You have provided {q=}"}
    else:
        return {
            "message": "Following are the provided query parameters.",
            "skip": skip,
            "limit": limit,
            "category": category,
            "data": db[skip : skip + limit],
        }


# Reference: https://fastapi.tiangolo.com/tutorial/query-params/
