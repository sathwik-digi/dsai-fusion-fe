from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Enum,
    Boolean,
    ForeignKey,
    TIMESTAMP,
    JSON,
    Text,
    func
)
from sqlalchemy.orm import relationship
from app.db.database import Base


class IdpConfig(Base):
    __tablename__ = "idp_config"

    idp_id = Column(
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

    provider = Column(
        Enum("OKTA", "AZURE_AD", "KEYCLOAK", name="idp_provider_enum"),
        nullable=True
    )

    protocol = Column(
        Enum("OIDC", "SAML", name="idp_protocol_enum"),
        nullable=True
    )

    client_id = Column(
        String(255),
        nullable=True
    )

    client_secret_encrypted = Column(
        String(500),
        nullable=True
    )

    issuer_url = Column(
        String(500),
        nullable=True
    )

    redirect_url = Column(
        String(500),
        nullable=True
    )

    scopes = Column(
        JSON,
        nullable=True
    )

    metadata_xml = Column(
        Text,
        nullable=True
    )

    config_json = Column(
        JSON,
        nullable=True
    )

    is_enabled = Column(
        Boolean,
        nullable=True
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    # Relationship
    fusion_config = relationship(
        "FusionConfig",
        back_populates="idp_configs"
    )