from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db

router = APIRouter()

# Create a new chat message
@router.post("/send_message")
def send_message(message: schemas.ChatMessageCreate, db: Session = Depends(get_db)):
    return services.chat_service.create_message(db, message)

# Get all chat messages
@router.get("/messages")
def get_messages(db: Session = Depends(get_db)):
    return services.chat_service.get_messages(db)

# Get a single message by ID
@router.get("/message/{message_id}")
def get_message(message_id: int, db: Session = Depends(get_db)):
    return services.chat_service.get_message(db, message_id)

# Delete a message by ID
@router.delete("/delete_message/{message_id}")
def delete_message(message_id: int, db: Session = Depends(get_db)):
    return services.chat_service.delete_message(db, message_id)
