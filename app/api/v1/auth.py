from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import LoginRequest, LoginResponse
from app.crud.user import authenticate_user
from app.crud.token import store_user_token
from app.db.session import get_db
from app.core.security import create_access_token


router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login(user_data: LoginRequest, db: Session = Depends(get_db)):

    user = authenticate_user(db, user_data.email, user_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

     # Fetch role from relationship
    if not user.roles:
        raise HTTPException(status_code=403, detail="User has no assigned role")

    # Assuming one role per user
    role_name = user.roles[0].role_name

    token = create_access_token(
        data={"sub": user.email, "role": role_name}
    )

    # Store token in DB
    store_user_token(db, user.user_id, token)

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": role_name
    }