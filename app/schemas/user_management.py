from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class RoleType(str, Enum):
    PROVIDER = "SUPER_ADMIN"
    CUSTOMER = "CUSTOMER_ADMIN"
    USER = "END_USER"


class CreateUserRequest(BaseModel):
    role: RoleType

    # User details
    first_name: str
    last_name: str
    username: str
    password: str
    email: EmailStr

    # Required only if creating CUSTOMER
    customer_id: Optional[str] = None


class CreateUserResponse(BaseModel):
    user_id: int
    role: str
    customer_id: Optional[int] = None
    message: str