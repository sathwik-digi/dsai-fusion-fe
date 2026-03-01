from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.idp_config import IdpConfig
from app.models.fusion_config import FusionConfig
from app.models.user import User


def create_idp_config(db: Session, data, current_user: User):

    role_names = [role.role_name for role in current_user.roles]

    if "SUPER_ADMIN" in role_names:
        if not data.customer_id:
            raise HTTPException(status_code=400, detail="customer_id required for SUPER_ADMIN")

        fusion = db.query(FusionConfig).filter(
            FusionConfig.fusion_config_id == data.fusion_config_id,
            FusionConfig.customer_id == data.customer_id
        ).first()

        if not fusion:
            raise HTTPException(status_code=404, detail="Fusion config not found for this customer")

    elif "CUSTOMER_ADMIN" in role_names:
        fusion = db.query(FusionConfig).filter(
            FusionConfig.fusion_config_id == data.fusion_config_id,
            FusionConfig.customer_id == current_user.customer_id
        ).first()

        if not fusion:
            raise HTTPException(status_code=403, detail="Not allowed to use this fusion_config")

    else:
        raise HTTPException(status_code=403, detail="Unauthorized role")

    idp = IdpConfig(
        fusion_config_id=data.fusion_config_id,
        provider=data.provider,
        protocol=data.protocol,
        client_id=data.client_id,
        client_secret_encrypted=data.client_secret_encrypted,
        issuer_url=data.issuer_url,
        redirect_url=data.redirect_url,
        scopes=data.scopes,
        metadata_xml=data.metadata_xml,
        config_json=data.config_json,
        is_enabled=data.is_enabled
    )

    db.add(idp)
    db.commit()
    db.refresh(idp)

    return idp


def get_idp_config(db: Session, idp_id: int):
    idp = db.query(IdpConfig).filter(IdpConfig.idp_id == idp_id).first()

    if not idp:
        raise HTTPException(status_code=404, detail="IDP config not found")

    return idp


def get_all_idp_configs(db: Session):
    return db.query(IdpConfig).all()


def update_idp_config(db: Session, idp_id: int, data):
    idp = db.query(IdpConfig).filter(IdpConfig.idp_id == idp_id).first()

    if not idp:
        raise HTTPException(status_code=404, detail="IDP config not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(idp, key, value)

    db.commit()
    db.refresh(idp)

    return idp


def delete_idp_config(db: Session, idp_id: int):
    idp = db.query(IdpConfig).filter(IdpConfig.idp_id == idp_id).first()

    if not idp:
        raise HTTPException(status_code=404, detail="IDP config not found")

    db.delete(idp)
    db.commit()

    return {"message": "IDP config deleted successfully"}