from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.idp_config import (
    IdpConfigCreate,
    IdpConfigUpdate,
    IdpConfigResponse
)
from app.crud.idp_config import (
    create_idp_config,
    get_idp_config,
    get_all_idp_configs,
    update_idp_config,
    delete_idp_config
)

router = APIRouter()


@router.post("/", response_model=IdpConfigResponse)
def create(
    data: IdpConfigCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_idp_config(db, data, current_user)


@router.get("/{idp_id}", response_model=IdpConfigResponse)
def get_one(
    idp_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_idp_config(db, idp_id)


@router.get("/", response_model=list[IdpConfigResponse])
def get_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_idp_configs(db)


@router.put("/{idp_id}", response_model=IdpConfigResponse)
def update(
    idp_id: int,
    data: IdpConfigUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_idp_config(db, idp_id, data)


@router.delete("/{idp_id}")
def delete(
    idp_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_idp_config(db, idp_id)