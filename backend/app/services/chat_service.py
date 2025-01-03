from app import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException

# Create a chat message
def create_message(db: Session, message: schemas.ChatMessageCreate):
    db_message = models.ChatMessage(content=message.content, user_id=message.user_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

# Read all messages for a chat
def get_messages(db: Session):
    return db.query(models.ChatMessage).all()

# Read a specific message
def get_message(db: Session, message_id: int):
    return db.query(models.ChatMessage).filter(models.ChatMessage.id == message_id).first()

# Delete a message
def delete_message(db: Session, message_id: int):
    db_message = db.query(models.ChatMessage).filter(models.ChatMessage.id == message_id).first()
    if db_message:
        db.delete(db_message)
        db.commit()
        return {"message": "Message deleted"}
    else:
        raise HTTPException(status_code=404, detail="Message not found")
