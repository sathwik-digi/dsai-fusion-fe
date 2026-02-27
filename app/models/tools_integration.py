from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Text,
    Enum,
    ForeignKey,
    TIMESTAMP,
    func,
)

from app.db.database import Base
from sqlalchemy.orm import relationship


class ToolsIntegration(Base):
    __tablename__ = "tools_integration"

    tool_id = Column(BigInteger, primary_key=True, autoincrement=True)
    customer_id = Column(
        BigInteger,
        ForeignKey("customers.customer_id"),
        nullable=True,
        index=True,
    )
    tool_name = Column(String(255), nullable=True)
    environment = Column(
        Enum("DEV", "QA", "PROD", name="environment_enum"),
        nullable=True,
    )
    key_name = Column(String(255), nullable=True)
    api_key_encrypted = Column(Text, nullable=True)
    created_at = Column(
        TIMESTAMP,
        nullable=True,
        server_default=func.current_timestamp(),
    )
    expires_at = Column(TIMESTAMP, nullable=True)

    # Optional relationship (if you have Customer model)
    customer = relationship("Customer", back_populates="tools_integrations")