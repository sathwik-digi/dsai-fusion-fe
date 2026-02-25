from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.data_model import (
    DataModelCreate,
    DataModelUpdate,
    DataModelResponse
)
from app.crud.data_model import (
    create_data_model,
    get_data_model,
    get_all_data_models,
    update_data_model,
    delete_data_model
)

router = APIRouter()


@router.post("/", response_model=DataModelResponse)
def create(
    data: DataModelCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_data_model(db, data, current_user)


@router.get("/{data_model_id}", response_model=DataModelResponse)
def get_one(
    data_model_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_data_model(db, data_model_id)


@router.get("/", response_model=list[DataModelResponse])
def get_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_data_models(db)


@router.put("/{data_model_id}", response_model=DataModelResponse)
def update(
    data_model_id: int,
    data: DataModelUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_data_model(db, data_model_id, data)


@router.delete("/{data_model_id}")
def delete(
    data_model_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_data_model(db, data_model_id)