"""
The file app/routers/items.py is inside a package, app/routers/, so, it's a submodule: app.routers.items
Notes:
- We know all the path operations in this module have the same:
  - Path prefix: /items.
  - tags: (just one tag: items).
  - Extra responses.
  - dependencies: they all need that X-Token dependency we created.
- So, instead of adding all that to each path operation, we can add it to the APIRouter.
"""

from fastapi import APIRouter, Depends, HTTPException
from structure.dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["Items"],
    dependencies=[Depends(get_token_header)],
)

fake_db = {
    "http": {"protocol_code": 1, "protocol_usage": "Web", "is_recommended": False},
    "https": {"protocol_code": 2, "protocol_usage": "Web", "is_recommended": True},
}


@router.get(path="/")
async def read_items():
    return fake_db


@router.get(path="/{protocol}")
async def read_item(protocol: str):
    try:
        item = fake_db[protocol]
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="Item does not exists. Valid items are (http, https)",
        )
    else:
        return item


@router.put(
    path="/{protocol}",
    tags=["Owner"],
    responses={
        403: {"description": "Operation forbidden"},
        404: {"description": "Resource not found"},
    },
)
async def update_item(protocol: str):
    if protocol in ("GlobalAdmin", "OrganizationAdmin"):
        raise HTTPException(
            status_code=403,
            detail=f"You can't process entity with {protocol}. Use different string.",
        )
    if protocol not in fake_db:
        raise HTTPException(
            status_code=404,
            detail="Item does not exists. Valid items are (http, https)",
        )
    return {"protocol": protocol, "message": "Item has been updated successfully."}
