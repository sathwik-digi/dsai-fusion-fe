from sqlalchemy import (
    Column,
    BigInteger,
    String,
    ForeignKey,
    TIMESTAMP,
    func
)
from sqlalchemy.orm import relationship
from app.db.database import Base


class UserToken(Base):
    __tablename__ = "user_tokens"

    token_id = Column(BigInteger, primary_key=True, index=True)

    user_id = Column(
        BigInteger,
        ForeignKey("users.user_id"),
        nullable=True
    )

    token = Column(String(500), nullable=True)

    token_expiration_time = Column(TIMESTAMP, nullable=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )

    # Relationship
    user = relationship("User", back_populates="tokens")
