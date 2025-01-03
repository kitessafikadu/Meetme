from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db

router = APIRouter()

# Create Notification
@router.post("/", response_model=schemas.NotificationResponse)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db)):
    db_notification = services.notifications_service.create_notification(db=db, notification=notification)
    return db_notification

# Get All Notifications
@router.get("/", response_model=list[schemas.NotificationResponse])
def get_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notifications = services.notifications_service.get_notifications(db=db, skip=skip, limit=limit)
    return notifications

# Get a Single Notification
@router.get("/{notification_id}", response_model=schemas.NotificationResponse)
def get_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = services.notifications_service.get_notification(db=db, notification_id=notification_id)
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

# Update Notification Status
@router.put("/{notification_id}", response_model=schemas.NotificationResponse)
def update_notification_status(notification_id: int, is_read: bool, db: Session = Depends(get_db)):
    notification = services.notifications_service.update_notification_status(db=db, notification_id=notification_id, is_read=is_read)
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

# Delete Notification
@router.delete("/{notification_id}", response_model=schemas.NotificationResponse)
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = services.notifications_service.delete_notification(db=db, notification_id=notification_id)
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification
