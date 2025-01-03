from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db

router = APIRouter()

# Create a new group
@router.post("/create")
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    return services.group_service.create_group(db, group)

# Get group by ID
@router.get("/{group_id}")
def get_group(group_id: int, db: Session = Depends(get_db)):
    return services.group_service.get_group(db, group_id)

# Get all groups
@router.get("/")
def get_all_groups(db: Session = Depends(get_db)):
    return services.group_service.get_all_groups(db)

# Update group
@router.put("/{group_id}")
def update_group(group_id: int, group: schemas.GroupCreate, db: Session = Depends(get_db)):
    return services.group_service.update_group(db, group_id, group)

# Delete group
@router.delete("/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db)):
    return services.group_service.delete_group(db, group_id)
