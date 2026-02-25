from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Boolean,
    Enum,
    ForeignKey,
    TIMESTAMP,
    JSON,
    func
)
from sqlalchemy.orm import relationship
from app.db.database import Base


class DataModel(Base):
    __tablename__ = "data_models"

    data_model_id = Column(
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

    data_model_name = Column(
        String(255),
        nullable=True
    )

    data_model_version = Column(
        String(50),
        nullable=True
    )

    storage_type = Column(
        Enum("S3", "DB", "FILESYSTEM", name="storage_type_enum"),
        nullable=True
    )

    # tinyint(1) → Boolean
    is_active = Column(
        Boolean,
        nullable=True
    )

    model_metadata = Column("metadata", JSON, nullable=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    # Relationship with FusionConfig
    fusion_config = relationship(
        "FusionConfig",
        back_populates="data_models"
    )