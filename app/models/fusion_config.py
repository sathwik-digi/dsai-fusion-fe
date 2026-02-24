from sqlalchemy import (
    Column,
    BigInteger,
    Boolean,
    Enum,
    ForeignKey,
    TIMESTAMP,
    func
)
from sqlalchemy.orm import relationship
from app.db.database import Base


class FusionConfig(Base):
    __tablename__ = "fusion_config"

    fusion_config_id = Column(
        BigInteger,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    customer_id = Column(
        BigInteger,
        ForeignKey("customers.customer_id"),
        nullable=True
    )

    external_auth_required = Column(
        Boolean,
        nullable=True
    )

    environment = Column(
        Enum("DEV", "QA", "PROD", name="environment_enum"),
        nullable=True
    )

    status = Column(
        Enum("ACTIVE", "INACTIVE", name="fusion_status_enum"),
        nullable=True
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

    # Relationships

    customer = relationship(
        "Customer",
        back_populates="fusion_configs"
    )

    services = relationship(
        "ServiceEnablement",
        back_populates="fusion_config",
        cascade="all, delete-orphan"
    )