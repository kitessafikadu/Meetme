from app import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException

# Create Group
def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

# Get Group by ID
def get_group(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).first()

# Get all groups
def get_all_groups(db: Session):
    return db.query(models.Group).all()

# Update Group
def update_group(db: Session, group_id: int, group_data: schemas.GroupCreate):
    db_group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if db_group:
        db_group.name = group_data.name
        db.commit()
        db.refresh(db_group)
        return db_group
    else:
        raise HTTPException(status_code=404, detail="Group not found")

# Delete Group
def delete_group(db: Session, group_id: int):
    db_group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if db_group:
        db.delete(db_group)
        db.commit()
        return {"message": "Group deleted"}
    else:
        raise HTTPException(status_code=404, detail="Group not found")
