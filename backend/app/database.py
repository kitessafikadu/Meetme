from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from fastapi import  Depends
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db(db: Session = Depends(SessionLocal)):
    try:
        yield db
    finally:
        db.close()

def create_db():
    Base.metadata.create_all(bind=engine)

create_db()
