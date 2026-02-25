from pydantic import BaseModel
from typing import Optional, Dict


class DataModelCreate(BaseModel):
    fusion_config_id: int
    data_model_name: str
    data_model_version: str
    storage_type: str
    is_active: bool
    model_metadata: Optional[Dict] = None
    customer_id: Optional[int] = None  # Required only for SUPER_ADMIN


class DataModelUpdate(BaseModel):
    data_model_name: Optional[str] = None
    data_model_version: Optional[str] = None
    storage_type: Optional[str] = None
    is_active: Optional[bool] = None
    model_metadata: Optional[Dict] = None


class DataModelResponse(BaseModel):
    data_model_id: int
    fusion_config_id: int
    data_model_name: str
    data_model_version: str
    storage_type: str
    is_active: bool
    model_metadata: Optional[Dict]

    class Config:
        from_attributes = True