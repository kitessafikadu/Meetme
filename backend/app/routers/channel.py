from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db

router = APIRouter()

# Create a new channel
@router.post("/create")
def create_channel(channel: schemas.ChannelCreate, db: Session = Depends(get_db)):
    return services.channel_service.create_channel(db, channel)

# Get channel by ID
@router.get("/{channel_id}")
def get_channel(channel_id: int, db: Session = Depends(get_db)):
    return services.channel_service.get_channel(db, channel_id)

# Get all channels
@router.get("/")
def get_all_channels(db: Session = Depends(get_db)):
    return services.channel_service.get_all_channels(db)

# Update channel
@router.put("/{channel_id}")
def update_channel(channel_id: int, channel: schemas.ChannelCreate, db: Session = Depends(get_db)):
    return services.channel_service.update_channel(db, channel_id, channel)

# Delete channel
@router.delete("/{channel_id}")
def delete_channel(channel_id: int, db: Session = Depends(get_db)):
    return services.channel_service.delete_channel(db, channel_id)
