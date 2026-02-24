from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Enum,
    TIMESTAMP,
    func
)
from sqlalchemy.orm import relationship
from app.db.database import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(
        BigInteger,
        primary_key=True,
        index=True
    )

    customer_code = Column(String(100), nullable=True)
    customer_name = Column(String(255), nullable=False)
    contact_email = Column(String(255), nullable=True)
    contact_phone = Column(String(50), nullable=True)
    contact_address = Column(String(512), nullable=True)

    status = Column(
        Enum("ACTIVE", "INACTIVE", "SUSPENDED", name="customer_status_enum"),
        default="ACTIVE"
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )

    # Relationship with Users
    users = relationship("User", back_populates="customer")

    fusion_configs = relationship(
        "FusionConfig",
        back_populates="customer",
        cascade="all, delete-orphan"
    )