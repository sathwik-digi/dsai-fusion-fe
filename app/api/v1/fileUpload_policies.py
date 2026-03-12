from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.schemas.fileUpload_policies import FileUplaodCreateRequest, FileUplaodCreateResponse
from app.crud import fileUpload_Policies as crud

router = APIRouter(tags=["File Upload Policies"])

@router.post("/create", response_model=FileUplaodCreateResponse, status_code=status.HTTP_201_CREATED)
def create_File_Uplaod_Policies(
    payload: FileUplaodCreateRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return crud.createFileUplaodPolicies(db, current_user.customer_id, payload)

@router.get("/getAllPrinciples",response_model=List[FileUplaodCreateResponse],status_code=status.HTTP_200_OK)
def getAll_FileUpload_Policies(
    db: Session = Depends(get_db),
):
    return crud.getAll_FileUpload_Policies(db)

@router.get("/getPoliciesByCustomerId",response_model=List[FileUplaodCreateResponse],status_code=status.HTTP_200_OK)
def get_FileUploadPoliciesByCustomerId(
    db:Session=Depends(get_db),
    current_user=Depends(get_current_user),
):
    return crud.get_FileUpload_PoliciesByCustomerId(db,current_user.customer_id)

@router.get("/getPolicyByPolicyId", response_model=List[FileUplaodCreateResponse],status_code=status.HTTP_200_OK)
def getPolicyByPolicyId(
    policy_id: int,
    db:Session=Depends(get_db),
):
    return crud.getPolicyByPolicyId(db,policy_id)

@router.put("/updatePolicyById", response_model=FileUplaodCreateResponse, status_code=status.HTTP_200_OK)
def updatePolicyById(
    payload:FileUplaodCreateRequest,
    policyId :int,
    db:Session = Depends(get_db),
):
    return crud.updatePolicyById(payload,policyId,db)

@router.delete("/deletePolicyById", status_code=status.HTTP_200_OK)
def delete_policy_by_id(
    policyId: int,
    db: Session = Depends(get_db)
):
    return crud.deletePolicyById(db, policyId)