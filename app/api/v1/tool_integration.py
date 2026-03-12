from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.tools_integration import (
    ToolsIntegrationCreate,
    ToolsIntegrationUpdate,
    ToolsIntegrationResponse,
)
from app.dependencies.auth import get_current_user
from app.crud import tools_integration as crud

router = APIRouter(tags=["Tools Integration"])


@router.post(
    "/createTool",
    response_model=ToolsIntegrationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_tools_integration(
    payload: ToolsIntegrationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return crud.create_tool(db, current_user.customer_id, payload)


@router.get("/getAllTools", response_model=List[ToolsIntegrationResponse])
def get_my_tools_integrations(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return crud.get_all_tools(db, current_user.customer_id)


@router.get("/getToolById/{tool_id}", response_model=ToolsIntegrationResponse)
def get_tools_integration(
    tool_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    record = crud.get_tool_by_id(db, tool_id, current_user.customer_id)

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    return record


@router.put("/updateToolByID/{tool_id}", response_model=ToolsIntegrationResponse)
def update_tools_integration(
    tool_id: int,
    payload: ToolsIntegrationUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    record = crud.get_tool_by_id(db, tool_id, current_user.customer_id)

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    return crud.update_tool(db, record, payload)


from fastapi import status, HTTPException, Depends
from sqlalchemy.orm import Session

@router.delete("/deleteToolById/{tool_id}", status_code=status.HTTP_200_OK)
def delete_tools_integration(
    tool_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    record = crud.get_tool_by_id(db, tool_id, current_user.customer_id)

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    message = crud.delete_tool(db, record)
    return {"message": message}