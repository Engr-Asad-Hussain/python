"""
The same with app/routers/users.py, it's another submodule: app.routers.users
Notes:
- Let's say the file dedicated to handling just users is the submodule at /app/routers/users.py.
- You want to have the path operations related to your users separated from the rest of the code, 
  to keep it organized.
- But it's still part of the same FastAPI application/web API (it's part of the same "Python Package").
- You can create the path operations for that module using APIRouter
"""

from fastapi import APIRouter

router = APIRouter()


@router.get(path="/users", tags=["Users"], response_model=list[str])
async def read_users():
    return ["Asad Hussain", "Danish Khalid", "Junaid Akram"]


@router.get(path="/users/me", tags=["Users"])
async def read_users_me():
    return {"name": "Asad Hussain"}


@router.get(path="/users/{user_id}")
async def read_user(user_id: int):
    return {"name": "Asad Hussain", "id": user_id}
