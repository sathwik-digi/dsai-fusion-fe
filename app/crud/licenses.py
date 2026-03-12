from sqlalchemy.orm import Session

from app.models.licenses import Licenses


def createLicense(db:Session ,data, customerId :int ):

    db_obj = Licenses(
        customer_id=customerId,
        api_key=data.api_key,
        api_key_type=data.api_key_type,
        plan=data.plan,
        environment=data.environment,
        start_date=data.start_date,
        end_date=data.end_date,
        max_users=data.max_users,
        status=data.status
)
   
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def getLicenseById(license_Id:int,db:Session):
    return db.query(Licenses).filter(Licenses.license_id==license_Id).first()

def getAllLicenses(db:Session):
    return db.query(Licenses).all()

def updateLicenseById(data,db:Session,license_Id:int):
    db_obj = db.query(Licenses).filter(
        Licenses.license_id == license_Id
    ).first()

    if not db_obj:
        return None
   
    db_obj.api_key=data.api_key
    db_obj.api_key_type=data.api_key_type
    db_obj. plan=data.plan
    db_obj.environment=data.environment
    db_obj.start_date=data.start_date
    db_obj.end_date=data.end_date
    db_obj. max_users=data.max_users
    db_obj. status=data.status

    db.commit()
    db.refresh(db_obj)
    return db_obj

def deleteLicenseById(license_Id :int,db:Session):
    db_Obj=db.query(Licenses).filter(Licenses.license_id==license_Id).first()

    if not db_Obj:
        return None 
    db.delete(db_Obj)
    db.commit()
    return "Deleted Successfully"
     