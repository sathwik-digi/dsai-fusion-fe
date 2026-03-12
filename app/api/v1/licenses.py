from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.licenses import LicenseCreateRequest, LicenseResponse
from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.crud import licenses as crud

router = APIRouter(tags=["Licenses"])

@router.post("/addLicense",response_model=LicenseResponse, status_code=status.HTTP_201_CREATED)
def createLicense(
        payload:LicenseCreateRequest,
        db:Session=Depends(get_db),
        current_user=Depends(get_current_user)
):
    return crud.createLicense(db,payload,current_user.customer_id)

@router.get("/getLicenseById",response_model=LicenseResponse, status_code=status.HTTP_200_OK)
def getLicenseById(
    license_Id : int,
    db:Session=Depends(get_db)
):
    return crud.getLicenseById(license_Id,db)

@router.get("/getAllLicense",response_model=List[LicenseResponse],status_code=status.HTTP_200_OK)
def getAllLicenses(
    db:Session=Depends(get_db)
):
    return crud.getAllLicenses(db)

@router.put("/updateLicenseById",response_model=LicenseResponse,status_code=status.HTTP_200_OK)
def updateLicenseById(
    payload:LicenseCreateRequest,
    license_Id:int,
    db:Session=Depends(get_db)
):
    return crud.updateLicenseById(payload,db,license_Id)

@router.delete("/deleteLicenseById",status_code=status.HTTP_200_OK)
def deleteLicenseById(
    license_Id:int,
    db:Session=Depends(get_db)
):
    return crud.deleteLicenseById(license_Id,db)