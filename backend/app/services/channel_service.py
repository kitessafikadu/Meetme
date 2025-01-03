from app import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException

# Create Channel
def create_channel(db: Session, channel: schemas.ChannelCreate):
    db_channel = models.Channel(name=channel.name)
    db.add(db_channel)
    db.commit()
    db.refresh(db_channel)
    return db_channel

# Get Channel by ID
def get_channel(db: Session, channel_id: int):
    return db.query(models.Channel).filter(models.Channel.id == channel_id).first()

# Get all channels
def get_all_channels(db: Session):
    return db.query(models.Channel).all()

# Update Channel
def update_channel(db: Session, channel_id: int, channel_data: schemas.ChannelCreate):
    db_channel = db.query(models.Channel).filter(models.Channel.id == channel_id).first()
    if db_channel:
        db_channel.name = channel_data.name
        db.commit()
        db.refresh(db_channel)
        return db_channel
    else:
        raise HTTPException(status_code=404, detail="Channel not found")

# Delete Channel
def delete_channel(db: Session, channel_id: int):
    db_channel = db.query(models.Channel).filter(models.Channel.id == channel_id).first()
    if db_channel:
        db.delete(db_channel)
        db.commit()
        return {"message": "Channel deleted"}
    else:
        raise HTTPException(status_code=404, detail="Channel not found")
