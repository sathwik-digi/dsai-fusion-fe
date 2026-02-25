from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.data_model import DataModel
from app.models.fusion_config import FusionConfig
from app.models.user import User


def create_data_model(db: Session, data, current_user: User):

    role_names = [role.role_name for role in current_user.roles]

    # SUPER_ADMIN must pass customer_id
    if "SUPER_ADMIN" in role_names:
        if not data.customer_id:
            raise HTTPException(status_code=400, detail="customer_id required for SUPER_ADMIN")

        fusion = db.query(FusionConfig).filter(
            FusionConfig.fusion_config_id == data.fusion_config_id,
            FusionConfig.customer_id == data.customer_id
        ).first()

        if not fusion:
            raise HTTPException(status_code=404, detail="Fusion config not found for this customer")

    # CUSTOMER_ADMIN auto-detect
    elif "CUSTOMER_ADMIN" in role_names:
        fusion = db.query(FusionConfig).filter(
            FusionConfig.fusion_config_id == data.fusion_config_id,
            FusionConfig.customer_id == current_user.customer_id
        ).first()

        if not fusion:
            raise HTTPException(status_code=403, detail="Not allowed to use this fusion_config")

    else:
        raise HTTPException(status_code=403, detail="Unauthorized role")

    model = DataModel(
        fusion_config_id=data.fusion_config_id,
        data_model_name=data.data_model_name,
        data_model_version=data.data_model_version,
        storage_type=data.storage_type,
        is_active=data.is_active,
        model_metadata=data.model_metadata
    )

    db.add(model)
    db.commit()
    db.refresh(model)

    return model


def get_data_model(db: Session, data_model_id: int):
    model = db.query(DataModel).filter(
        DataModel.data_model_id == data_model_id
    ).first()

    if not model:
        raise HTTPException(status_code=404, detail="Data model not found")

    return model


def get_all_data_models(db: Session):
    return db.query(DataModel).all()


def update_data_model(db: Session, data_model_id: int, data):
    model = db.query(DataModel).filter(
        DataModel.data_model_id == data_model_id
    ).first()

    if not model:
        raise HTTPException(status_code=404, detail="Data model not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(model, key, value)

    db.commit()
    db.refresh(model)

    return model


def delete_data_model(db: Session, data_model_id: int):
    model = db.query(DataModel).filter(
        DataModel.data_model_id == data_model_id
    ).first()

    if not model:
        raise HTTPException(status_code=404, detail="Data model not found")

    db.delete(model)
    db.commit()

    return {"message": "Data model deleted successfully"}