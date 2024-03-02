from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


# Annotation on path parameters
# This way you can add numeric validation on path-parameters
@app.get(path="/api/category/{cloth_id}")
async def specific_category(
    cloth_id: Annotated[int, Path(title="Cloth Reference", ge=1)]
):
    return {"message": "Following is the provided path parameter", "clothId": cloth_id}


# Reference: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
