from pydantic import BaseModel
from typing import Optional


class RoleCreate(BaseModel):
    role_name: str
    role_scope: Optional[str] = None
    description: Optional[str] = None


class RoleUpdate(BaseModel):
    role_scope: Optional[str] = None
    description: Optional[str] = None


class RoleResponse(BaseModel):
    role_id: int
    role_name: str
    role_scope: Optional[str]
    description: Optional[str]

    class Config:
        from_attributes = True
