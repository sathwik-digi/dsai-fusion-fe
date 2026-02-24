from pydantic import BaseModel
from typing import Optional


class ServiceCreate(BaseModel):
    fusion_config_id: int
    service_code: str
    service_name: str
    is_enabled: bool
    customer_id: Optional[int] = None  # Required only for SUPER_ADMIN


class ServiceUpdate(BaseModel):
    service_code: Optional[str] = None
    service_name: Optional[str] = None
    is_enabled: Optional[bool] = None


class ServiceResponse(BaseModel):
    service_id: int
    fusion_config_id: int
    service_code: str
    service_name: str
    is_enabled: bool

    class Config:
        from_attributes = True