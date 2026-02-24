from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.service_enablement import ServiceEnablement
from app.models.fusion_config import FusionConfig
from app.models.user import User


def create_service(db: Session, data, current_user: User):

    # ROLE CHECK
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

    service = ServiceEnablement(
        fusion_config_id=data.fusion_config_id,
        service_code=data.service_code,
        service_name=data.service_name,
        is_enabled=data.is_enabled
    )

    db.add(service)
    db.commit()
    db.refresh(service)

    return service


def get_service(db: Session, service_id: int):
    service = db.query(ServiceEnablement).filter(
        ServiceEnablement.service_id == service_id
    ).first()

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    return service


def get_all_services(db: Session):
    return db.query(ServiceEnablement).all()


def update_service(db: Session, service_id: int, data):
    service = db.query(ServiceEnablement).filter(
        ServiceEnablement.service_id == service_id
    ).first()

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(service, key, value)

    db.commit()
    db.refresh(service)

    return service


def delete_service(db: Session, service_id: int):
    service = db.query(ServiceEnablement).filter(
        ServiceEnablement.service_id == service_id
    ).first()

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    db.delete(service)
    db.commit()

    return {"message": "Service deleted successfully"}