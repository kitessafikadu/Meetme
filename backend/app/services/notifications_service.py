from sqlalchemy.orm import Session
from app import models, schemas

# Create Notification
def create_notification(db: Session, notification: schemas.NotificationCreate):
    db_notification = models.Notification(
        title=notification.title,
        message=notification.message,
        user_id=notification.user_id
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

# Get All Notifications
def get_notifications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Notification).offset(skip).limit(limit).all()

# Get a Single Notification
def get_notification(db: Session, notification_id: int):
    return db.query(models.Notification).filter(models.Notification.id == notification_id).first()

# Update Notification Status
def update_notification_status(db: Session, notification_id: int, is_read: bool):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if db_notification:
        db_notification.is_read = is_read
        db.commit()
        db.refresh(db_notification)
    return db_notification

# Delete Notification
def delete_notification(db: Session, notification_id: int):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if db_notification:
        db.delete(db_notification)
        db.commit()
    return db_notification
