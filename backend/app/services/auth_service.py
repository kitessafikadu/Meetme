from app import models, schemas
from sqlalchemy.orm import Session
from app.core.security import create_access_token
from fastapi import HTTPException

# Create User
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password, first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Read User
def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Authenticate User
def authenticate_user(db: Session, credentials: schemas.UserCreate):
    user = db.query(models.User).filter(models.User.username == credentials.username).first()
    if not user or user.password != credentials.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return create_access_token({"sub": user.username})
