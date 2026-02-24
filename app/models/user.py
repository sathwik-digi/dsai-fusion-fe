from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Enum,
    ForeignKey,
    TIMESTAMP,
    func
)
from sqlalchemy.orm import relationship
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, index=True)

    customer_id = Column(
        BigInteger,
        ForeignKey("customers.customer_id"),
        nullable=True  # Changed: DB allows NULL
    )

    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)

    username = Column(String(100), unique=True, nullable=True)

    password_hash = Column(String(255), nullable=True)

    email = Column(String(255), nullable=True)

    status = Column(
        Enum("ACTIVE", "INACTIVE", name="user_status_enum"),
        nullable=True
    )

    last_login = Column(TIMESTAMP, nullable=True)

    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )
    customer = relationship("Customer", back_populates="users")

    # Relationship to Customer

    # One-to-many with user_roles

    user_roles = relationship(
        "UserRole",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    # Direct many-to-many access to roles
    roles = relationship(
        "Role",
        secondary="user_roles",
        back_populates="users",
        viewonly=True
    )

    tokens = relationship(
        "UserToken",
        back_populates="user",
        cascade="all, delete-orphan"
    )


# {
#     config = "324"
#     x = "2"
#     y = "3"

#     0
#     0

#     2
#     2

#     5
#     25

#     7
#     257

#     10
#     2570

#     12
#     25702

#     15
#     257025

# }