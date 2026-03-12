from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal


class FileUplaodCreateRequest(BaseModel):
    policy_name: Optional[str] = None
    policy_description: Optional[str] = None
    max_file_size_mb: Optional[int] = None
    allowed_file_types: Optional[List[str]] = None
    blocked_file_types: Optional[List[str]] = None
    max_files_per_user_daily: Optional[int] = None
    max_total_storage_gb: Optional[Decimal] = None
    require_virus_scan: Optional[bool] = False
    is_active: Optional[bool] = True


class FileUplaodCreateResponse(BaseModel):
    policy_id: int
    customer_id: int

    policy_name: Optional[str] = None
    policy_description: Optional[str] = None
    max_file_size_mb: Optional[int] = None
    allowed_file_types: Optional[List[str]] = None
    blocked_file_types: Optional[List[str]] = None
    max_files_per_user_daily: Optional[int] = None
    max_total_storage_gb: Optional[Decimal] = None
    require_virus_scan: Optional[bool] = None
    is_active: Optional[bool] = None

    class Config:
        from_attributes = True