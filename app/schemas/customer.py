from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional



class CustomerStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class CustomerCreate(BaseModel):

    # Admin User Details
    first_name: str
    last_name: str
    username: str
    password: str
    user_email: EmailStr

    # Company Details
    company_name: str
    address: str
    phone: str
    company_email: EmailStr

    # Default status
    status: CustomerStatus = CustomerStatus.INACTIVE



class CustomerResponse(BaseModel):
    customer_id: int
    customer_name: str
    contact_email: Optional[str]
    contact_phone: Optional[str]
    contact_address: Optional[str]
    status: str

    class Config:
        from_attributes = True  # Needed for SQLAlchemy model
