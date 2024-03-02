from fastapi import FastAPI, Query
from typing import Annotated, Any

app = FastAPI()


# Annotated can be used to add metadata to your parameters
# This way you can add string validation on query-parameters
@app.get(path="/api/category/cloths")
async def cloths(
    limit: int = ...,
    skip: Annotated[str | None, "Total items to skip"] = ...,
    q: Annotated[
        str | None,
        Query(max_length=20, min_length=5, pattern="^fixedquery$"),
    ] = None,
    shape: Annotated[list[str], Query()] = ["circle"],
    any_type: Annotated[
        list[Any],
        Query(
            title="Query String",
            description="Any datatype can be accepted to search in the database.",
            alias="any-type",
            deprecated=True,
        ),
    ] = ["Circle", 2],
    hidden_query: Annotated[
        str,
        Query(
            description="This argument will not be part of automatic documentation in reDoc & docs",
            include_in_schema=False,
        ),
    ] = "Jumpbox",
):
    return {
        "message": "Following are the cloths.",
        "q": q,
        "limit": limit,
        "skip": skip,
        "shape": shape,
        "anyType": any_type,
        "hidden_query": hidden_query,
    }


# References: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
