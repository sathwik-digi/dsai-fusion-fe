from pydantic import BaseModel
from typing import Optional


class FusionConfigCreate(BaseModel):
    external_auth_required: Optional[bool] = False
    environment: str
    status: str
    customer_id: Optional[int] = None  # Required for SUPER_ADMIN


class FusionConfigUpdate(BaseModel):
    external_auth_required: Optional[bool] = None
    environment: Optional[str] = None
    status: Optional[str] = None


class FusionConfigResponse(BaseModel):
    fusion_config_id: int
    customer_id: Optional[int]
    external_auth_required: Optional[bool]
    environment: Optional[str]
    status: Optional[str]

    class Config:
        from_attributes = True