from sqlalchemy import Column, BigInteger, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.db.database import Base


class UserRole(Base):
    __tablename__ = "user_roles"

    user_id = Column(
        BigInteger,
        ForeignKey("users.user_id"),
        primary_key=True
    )

    role_id = Column(
        BigInteger,
        ForeignKey("roles.role_id"),
        primary_key=True
    )

    assigned_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    # Relationships
    user = relationship("User", back_populates="user_roles")
    role = relationship("Role", back_populates="user_roles")
