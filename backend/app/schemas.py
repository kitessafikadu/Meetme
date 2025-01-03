from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User Create Schema
class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: Optional[str] = None
    password: str
    profile_picture: Optional[str] = None  # Optional for profile picture

class UserResponse(UserCreate):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Chat Message Create Schema
class ChatMessageCreate(BaseModel):
    content: str
    user_id: int

class ChatMessageResponse(ChatMessageCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Group Create Schema
class GroupCreate(BaseModel):
    name: str

class GroupResponse(GroupCreate):
    id: int

    class Config:
        orm_mode = True

# Channel Create Schema
class ChannelCreate(BaseModel):
    name: str

class ChannelResponse(ChannelCreate):
    id: int

    class Config:
        orm_mode = True

# Notification Create Schema
class NotificationCreate(BaseModel):
    title: str
    message: str
    user_id: int

# Notification Response Schema
class NotificationResponse(NotificationCreate):
    id: int
    is_read: bool

    class Config:
        orm_mode = True