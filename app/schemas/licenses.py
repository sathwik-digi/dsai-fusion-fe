from datetime import date
from typing import Optional

from pydantic import BaseModel


class LicenseCreateRequest(BaseModel):
    api_key: Optional[str] = None
    api_key_type: Optional[str] = None
    plan: Optional[str] = None
    environment: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    max_users: Optional[int] = None
    status: Optional[str] = None

class LicenseResponse(BaseModel):
    api_key: Optional[str] = None
    api_key_type: Optional[str] = None
    plan: Optional[str] = None
    environment: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    max_users: Optional[int] = None
    status: Optional[str] = None
