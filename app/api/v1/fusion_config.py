from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.fusion_config import (
    FusionConfigCreate,
    FusionConfigUpdate,
    FusionConfigResponse
)
from app.crud.fusion_config import (
    create_fusion_config,
    get_fusion_config,
    get_all_fusion_configs,
    update_fusion_config,
    delete_fusion_config
)

router = APIRouter()


@router.post("/", response_model=FusionConfigResponse)
def create(
    data: FusionConfigCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_fusion_config(db, data, current_user)


@router.get("/{fusion_config_id}", response_model=FusionConfigResponse)
def get_one(
    fusion_config_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_fusion_config(db, fusion_config_id)


@router.get("/", response_model=list[FusionConfigResponse])
def get_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_fusion_configs(db)


@router.put("/{fusion_config_id}", response_model=FusionConfigResponse)
def update(
    fusion_config_id: int,
    data: FusionConfigUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_fusion_config(db, fusion_config_id, data)


@router.delete("/{fusion_config_id}")
def delete(
    fusion_config_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_fusion_config(db, fusion_config_id)