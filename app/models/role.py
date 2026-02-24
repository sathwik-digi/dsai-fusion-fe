from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from app.db.database import Base


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(
        BigInteger,
        primary_key=True,
        index=True
    )

    role_name = Column(
        String(150),
        nullable=False,
        unique=True
    )

    role_scope = Column(
        String(500),
        nullable=True
    )

    description = Column(
        String(500),
        nullable=True
    )

    # Relationship to UserRole
    user_roles = relationship(
        "UserRole",
        back_populates = "role",
        cascade = "all, delete-orphan"
    )

    # Direct access to users (many-to-many)
    users = relationship(
        "User",
        secondary="user_roles",
        back_populates="roles",
        viewonly=True
    )