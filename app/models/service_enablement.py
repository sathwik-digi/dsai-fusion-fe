from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Boolean,
    ForeignKey,
    TIMESTAMP,
    func
)
from sqlalchemy.orm import relationship
from app.db.database import Base


class ServiceEnablement(Base):
    __tablename__ = "service_enablement"

    service_id = Column(
        BigInteger,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    fusion_config_id = Column(
        BigInteger,
        ForeignKey("fusion_config.fusion_config_id"),
        nullable=True
    )

    service_code = Column(
        String(100),
        nullable=True
    )

    service_name = Column(
        String(255),
        nullable=True
    )

    # tinyint(1) → Boolean in SQLAlchemy
    is_enabled = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    # Relationship (optional but recommended)
    fusion_config = relationship(
        "FusionConfig",
        back_populates="services"
    )

    
