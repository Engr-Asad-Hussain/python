import os
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql import curd, models, schemas
from sql.database import SessionLocal, engine

# In a very simplistic way create the database tables:
# Normally you would probably initialize your database (create tables, etc) with Alembic.
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


async def get_db():
    """
    We need to have an independent database session/connection (SessionLocal) per request, use
    the same session through all the request and then close it after the request is finished.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(path="/api/users", status_code=201, response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate, db: Annotated[Session, Depends(get_db)]
):
    existing = curd.get_user_by_email(db, user.email)
    if existing is not None:
        raise HTTPException(status_code=400, detail="User already exists.")
    return curd.create_user(db, user)


@app.get(path="/api/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = curd.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User does not exists.")
    return user


@app.get(path="/api/users", response_model=list[schemas.User])
async def read_users(db: Annotated[Session, Depends(get_db)]):
    return curd.get_users(db)


@app.post(
    path="/api/users/{user_id}/items",
    status_code=201,
    response_model=schemas.Item,
)
async def create_user_item(
    user_id: int, item: schemas.ItemCreate, db: Annotated[Session, Depends(get_db)]
):
    return curd.create_item(db, item, user_id)


@app.get("/api/items", response_model=list[schemas.Item])
async def read_items(
    db: Annotated[Session, Depends(get_db)], skip: int = 0, limit: int = 10
):
    return curd.get_items(db, skip, limit)


# For debugging
@app.get(path="/app/pid")
async def app_process() -> dict[str, int]:
    return {"processPid": os.getpid()}
