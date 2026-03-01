from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.fusion_config import FusionConfig
from app.models.user import User


def create_fusion_config(db: Session, data, current_user: User):

    role_names = [role.role_name for role in current_user.roles]

    if "SUPER_ADMIN" in role_names:
        if not data.customer_id:
            raise HTTPException(status_code=400, detail="customer_id required for SUPER_ADMIN")
        customer_id = data.customer_id

    elif "CUSTOMER_ADMIN" in role_names:
        customer_id = current_user.customer_id

    else:
        raise HTTPException(status_code=403, detail="Unauthorized role")

    fusion = FusionConfig(
        customer_id=customer_id,
        external_auth_required=data.external_auth_required,
        environment=data.environment,
        status=data.status
    )

    db.add(fusion)
    db.commit()
    db.refresh(fusion)

    return fusion


def get_fusion_config(db: Session, fusion_config_id: int):
    fusion = db.query(FusionConfig).filter(
        FusionConfig.fusion_config_id == fusion_config_id
    ).first()

    if not fusion:
        raise HTTPException(status_code=404, detail="Fusion config not found")

    return fusion


def get_all_fusion_configs(db: Session):
    return db.query(FusionConfig).all()


def update_fusion_config(db: Session, fusion_config_id: int, data):
    fusion = db.query(FusionConfig).filter(
        FusionConfig.fusion_config_id == fusion_config_id
    ).first()

    if not fusion:
        raise HTTPException(status_code=404, detail="Fusion config not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(fusion, key, value)

    db.commit()
    db.refresh(fusion)

    return fusion


def delete_fusion_config(db: Session, fusion_config_id: int):
    fusion = db.query(FusionConfig).filter(
        FusionConfig.fusion_config_id == fusion_config_id
    ).first()

    if not fusion:
        raise HTTPException(status_code=404, detail="Fusion config not found")

    db.delete(fusion)
    db.commit()

    return {"message": "Fusion config deleted successfully"}