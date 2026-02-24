from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.role import (
    RoleCreate,
    RoleUpdate,
    RoleResponse
)
from app.crud.role import (
    create_role,
    get_roles,
    update_role,
    delete_role
)

router = APIRouter()


# ✅ Create Role
@router.post("/", response_model=RoleResponse)
def add_role(
    data: RoleCreate,
    db: Session = Depends(get_db)
):
    return create_role(db, data)


# ✅ Get All Roles
@router.get("/", response_model=List[RoleResponse])
def list_roles(
    db: Session = Depends(get_db)
):
    return get_roles(db)


# ✅ Update Role
@router.put("/{role_id}", response_model=RoleResponse)
def edit_role(
    role_id: int,
    data: RoleUpdate,
    db: Session = Depends(get_db)
):
    return update_role(db, role_id, data)


# ✅ Delete Role
@router.delete("/{role_id}")
def remove_role(
    role_id: int,
    db: Session = Depends(get_db)
):
    return delete_role(db, role_id)
