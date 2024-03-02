from enum import Enum
from fastapi import FastAPI


app = FastAPI()


# Notice that the value your function received (and returned) is item_id, as a Python int,
# not a convention string path parameter.
# So, with that type declaration, FastAPI gives you automatic request "parsing".
@app.get(path="/api/items/{item_id}")
async def specific_item(item_id: int):
    return {"message": f"Following is the item reference id: {item_id}"}


# Order matters
# When creating path operations, you can find situations where you have a fixed path.
# Like /users/me, let's say that it's to get data about the current user.
# And then you can also have a path /users/{user_id} to get data about a specific user by some user ID.
# Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:


@app.get(path="/api/users/me")
def root_user():
    return {"message": "This is the root user."}


@app.get(path="/api/users/{user_id}")
async def specific_user(user_id: str):
    return {"message": f"This is the specific users ({user_id})"}


# File path as path parameter
@app.get(path="/api/models/{filepath:path}")
def models_path(filepath: str):
    return {"message": filepath}


class Models(str, Enum):
    """
    In this case, the Models enumeration inherits from both str and Enum.
    This means that each member of the enumeration is not only an enumeration value but also a string.
    This can be useful in situations where you want to treat the enumeration values as strings directly.
    For example, you can compare, concatenate, or perform other string operations directly on the
    enumeration values.
    Example:
    >>> model = Models.regression
    >>> model == "regression" # True
    >>> model.upper() # REGRESSION
    """

    regression = "regression"
    forest = "forest"
    classifier = "classifier"
    transformer = "transformer"


@app.get(path="/api/models/{model}")
def models(model: Models):
    if model is Models.regression:
        return {"message": "Regression is good for prediction."}

    if model == Models.forest:
        return {"message": f"{model.upper()} is best for graphical prediction."}

    return {"message": f"This is also good for your task: {model}.", "model": model}


# Reference: https://fastapi.tiangolo.com/tutorial/path-params/
