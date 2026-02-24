from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.schemas.service_enablement import (
    ServiceCreate,
    ServiceUpdate,
    ServiceResponse
)
from app.crud.service_enablement import (
    create_service,
    get_service,
    get_all_services,
    update_service,
    delete_service
)

router = APIRouter()


@router.post("/", response_model=ServiceResponse)
def create(
    data: ServiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_service(db, data, current_user)


@router.get("/{service_id}", response_model=ServiceResponse)
def get_one(
    service_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_service(db, service_id)


@router.get("/", response_model=list[ServiceResponse])
def get_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_services(db)


@router.put("/{service_id}", response_model=ServiceResponse)
def update(
    service_id: int,
    data: ServiceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_service(db, service_id, data)


@router.delete("/{service_id}")
def delete(
    service_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_service(db, service_id)