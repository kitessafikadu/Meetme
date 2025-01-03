from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db

router = APIRouter()

# User Registration (Create User)
@router.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.auth_service.create_user(db, user)

# User Login
@router.post("/login")
def login(credentials: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.auth_service.authenticate_user(db, credentials)
