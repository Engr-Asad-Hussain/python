""" 
By creating functions that are only dedicated to interacting with the database (get a user 
or an item) independent of your path operation function, you can more easily reuse them in multiple 
parts and also add unit tests for them.
"""

from sqlalchemy.orm import Session
from sql import models, schemas


def get_user(db: Session, user_id: int) -> models.User | None:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    new_user = models.User(email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session, skip: int = 0, limit: int = 10) -> list[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate, user_id: int):
    new_item = models.Item(**item.model_dump(), owner_id=user_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def get_items(db: Session, skip: int = 0, limit: int = 10) -> list[models.Item]:
    return db.query(models.Item).offset(skip).limit(limit).all()
