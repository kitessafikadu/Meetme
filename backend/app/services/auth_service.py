from app import models, schemas
from sqlalchemy.orm import Session
from app.core.security import create_access_token
from fastapi import HTTPException

from passlib.context import CryptContext
from sqlalchemy.exc import SQLAlchemyError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, user: schemas.UserCreate):
    try:
        if db.query(models.User).filter(models.User.username == user.username).first():
            raise ValueError("Username already exists")

        hashed_password = hash_password(user.password)

        db_user = models.User(
            username=user.username,
            password=hashed_password,
            first_name=user.first_name,
            last_name=user.last_name,
            profile_picture=user.profile_picture or "default.jpg"
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return {
            "id": db_user.id,
            "username": db_user.username,
            "first_name": db_user.first_name,
            "last_name": db_user.last_name,
        }
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError("Database error occurred") from e


# Read User
def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Authenticate User
def authenticate_user(db: Session, credentials: schemas.UserCreate):
    user = db.query(models.User).filter(models.User.username == credentials.username).first()
    if not user or user.password != credentials.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return create_access_token({"sub": user.username})
