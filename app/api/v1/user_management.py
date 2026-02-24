from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user_management import (
    CreateUserRequest,
    CreateUserResponse
)
from app.crud.user_management import create_account
from app.dependencies.auth import get_current_user  # JWT dependency
from app.models.user import User

router = APIRouter()

@router.post("/create", response_model = CreateUserResponse)
def create_user_account(
    data: CreateUserRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_account(db, data, current_user)