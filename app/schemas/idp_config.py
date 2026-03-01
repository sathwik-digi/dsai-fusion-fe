from pydantic import BaseModel
from typing import Optional, Dict, List


class IdpConfigCreate(BaseModel):
    fusion_config_id: int
    provider: str
    protocol: str
    client_id: Optional[str] = None
    client_secret_encrypted: Optional[str] = None
    issuer_url: Optional[str] = None
    redirect_url: Optional[str] = None
    scopes: Optional[List[str]] = None
    metadata_xml: Optional[str] = None
    config_json: Optional[Dict] = None
    is_enabled: Optional[bool] = False
    customer_id: Optional[int] = None  # Required only for SUPER_ADMIN


class IdpConfigUpdate(BaseModel):
    provider: Optional[str] = None
    protocol: Optional[str] = None
    client_id: Optional[str] = None
    client_secret_encrypted: Optional[str] = None
    issuer_url: Optional[str] = None
    redirect_url: Optional[str] = None
    scopes: Optional[List[str]] = None
    metadata_xml: Optional[str] = None
    config_json: Optional[Dict] = None
    is_enabled: Optional[bool] = None


class IdpConfigResponse(BaseModel):
    idp_id: int
    fusion_config_id: int
    provider: Optional[str]
    protocol: Optional[str]
    client_id: Optional[str]
    issuer_url: Optional[str]
    redirect_url: Optional[str]
    scopes: Optional[List[str]]
    metadata_xml: Optional[str]
    config_json: Optional[Dict]
    is_enabled: Optional[bool]

    class Config:
        from_attributes = True