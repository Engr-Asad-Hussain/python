from enum import Enum

from fastapi import FastAPI

app = FastAPI()


# Path Operation Configuration
# You can define the (HTTP) status_code to be used in the response of your path operation.
# You can add tags to your path operation, pass the parameter tags with a list of str (commonly just one str):
class OperationTag(Enum):
    Path = "Path Operations"


@app.get(
    path="/api/path/operations",
    status_code=200,
    tags=[OperationTag.Path],
    response_model=dict[str, str | list[str]],
    summary="This is a short summary of the endpoint",
    # description="This is the description detail of the endpoint. Alternatively use docstring",
    response_description="The path operation is successful",
    deprecated=True,
)
async def path_operations():
    """
    Create an item with all the information:\n
    - name: each item must have a name
    - description: a long description
    - price: required
    - tax: if the item doesn't have tax, you can omit this
    - tags: a set of unique tag strings for this item
    """

    return {
        "message": "Following are the path operations",
        "operations": [
            "status_code",
            "tags",
            "response_model",
            "summary",
            "description",
            "response_description",
            "depreciated",
        ],
    }


# Reference: https://fastapi.tiangolo.com/tutorial/path-operation-configuration/
