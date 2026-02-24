from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.role import Role
from app.models.user_role import UserRole
from app.schemas.role import RoleCreate, RoleUpdate



def create_role(db: Session, data: RoleCreate):
    existing = db.query(Role).filter(Role.role_name == data.role_name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Role already exists")

    new_role = Role(
        role_name=data.role_name,
        role_scope=data.role_scope,
        description=data.description
    )

    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return new_role


def get_roles(db: Session):
    return db.query(Role).all()


def update_role(db: Session, role_id: int, data: RoleUpdate):
    role = db.query(Role).filter(Role.role_id == role_id).first()

    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    if data.role_scope is not None:
        role.role_scope = data.role_scope

    if data.description is not None:
        role.description = data.description

    db.commit()
    db.refresh(role)

    return role


def delete_role(db: Session, role_id: int):

    role = db.query(Role).filter(Role.role_id == role_id).first()

    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    # 🔍 Check if role is assigned to any user
    role_in_use = (
        db.query(UserRole)
        .filter(UserRole.role_id == role_id)
        .first()
    )

    if role_in_use:
        raise HTTPException(
            status_code=400,
            detail="Cannot delete role. Role is assigned to one or more users."
        )

    # ✅ Safe to delete
    db.delete(role)
    db.commit()

    return {"message": "Role deleted successfully"}
