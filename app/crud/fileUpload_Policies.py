from sqlalchemy.orm import Session
from app.models.fileUpload_policies import fileUploadPolicies


def createFileUplaodPolicies(db: Session, customer_id: int, data):
    db_obj = fileUploadPolicies(
        customer_id=customer_id,
        policy_name=data.policy_name,
        policy_description=data.policy_description,
        max_file_size_mb=data.max_file_size_mb,
        allowed_file_types=data.allowed_file_types,
        blocked_file_types=data.blocked_file_types,
        max_files_per_user_daily=data.max_files_per_user_daily,
        max_total_storage_gb=data.max_total_storage_gb,
        require_virus_scan=data.require_virus_scan,
        is_active=data.is_active,
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj

def getAll_FileUpload_Policies(db: Session):
    return db.query(fileUploadPolicies).all()

def get_FileUpload_PoliciesByCustomerId(db:Session,customerId):
    return db.query(fileUploadPolicies).filter(fileUploadPolicies.customer_id==customerId).all()

def getPolicyByPolicyId(db:Session,policyId):
    return db.query(fileUploadPolicies).filter(fileUploadPolicies.policy_id==policyId).all()

def updatePolicyById(data, policyId: int, db: Session):
    db_obj = db.query(fileUploadPolicies).filter(
        fileUploadPolicies.policy_id == policyId
    ).first()

    if not db_obj:
        return None

    db_obj.policy_name = data.policy_name
    db_obj.policy_description = data.policy_description
    db_obj.max_file_size_mb = data.max_file_size_mb
    db_obj.allowed_file_types = data.allowed_file_types
    db_obj.blocked_file_types = data.blocked_file_types
    db_obj.max_files_per_user_daily = data.max_files_per_user_daily
    db_obj.max_total_storage_gb = data.max_total_storage_gb
    db_obj.require_virus_scan = data.require_virus_scan
    db_obj.is_active = data.is_active

    db.commit()
    db.refresh(db_obj)

    return db_obj

def deletePolicyById(db: Session, policyId: int):
    db.query(fileUploadPolicies).filter(
        fileUploadPolicies.policy_id == policyId
    ).delete()

    db.commit()

    return "Deleted Successfully"