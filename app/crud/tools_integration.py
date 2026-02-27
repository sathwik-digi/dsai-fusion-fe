from sqlalchemy.orm import Session
from app.models.tools_integration import ToolsIntegration


def create_tool(db: Session, customer_id: int, data):
    db_obj = ToolsIntegration(
        customer_id=customer_id,
        tool_name=data.tool_name,
        environment=data.environment,
        key_name=data.key_name,
        api_key_encrypted=data.api_key_encrypted,
        expires_at=data.expires_at,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_all_tools(db: Session, customer_id: int):
    return (
        db.query(ToolsIntegration)
        .filter(ToolsIntegration.customer_id == customer_id)
        .all()
    )


def get_tool_by_id(db: Session, tool_id: int, customer_id: int):
    return (
        db.query(ToolsIntegration)
        .filter(
            ToolsIntegration.tool_id == tool_id,
            ToolsIntegration.customer_id == customer_id,
        )
        .first()
    )


def update_tool(db: Session, db_obj, data):
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_tool(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
    return "Deleted successfully"