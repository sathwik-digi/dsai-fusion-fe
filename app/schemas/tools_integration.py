from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class EnvironmentEnum(str, Enum):
    DEV = "DEV"
    QA = "QA"
    PROD = "PROD"


# 🔹 Create
class ToolsIntegrationCreate(BaseModel):
    tool_name: Optional[str] = None
    environment: Optional[EnvironmentEnum] = None
    key_name: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    expires_at: Optional[datetime] = None


# 🔹 Update
class ToolsIntegrationUpdate(BaseModel):
    tool_name: Optional[str] = None
    environment: Optional[EnvironmentEnum] = None
    key_name: Optional[str] = None
    api_key_encrypted: Optional[str] = None
    expires_at: Optional[datetime] = None


# 🔹 Response
class ToolsIntegrationResponse(BaseModel):
    tool_id: int
    customer_id: Optional[int]
    tool_name: Optional[str]
    environment: Optional[EnvironmentEnum]
    key_name: Optional[str]
    api_key_encrypted: Optional[str]
    created_at: Optional[datetime]
    expires_at: Optional[datetime]

    class Config:
        from_attributes = True