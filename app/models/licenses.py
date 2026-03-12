from sqlalchemy import Column, BigInteger, String, Integer, Date, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base


class Licenses(Base):
    __tablename__ = "licenses"

    license_id = Column(BigInteger, primary_key=True, autoincrement=True)

    customer_id = Column(BigInteger, ForeignKey("customers.customer_id"), nullable=False)

    api_key = Column(String(255), nullable=True)

    api_key_type = Column(
        Enum("INTERNAL", "EXTERNAL", name="api_key_type_enum"),
        nullable=True
    )

    plan = Column(String(100), nullable=True)

    environment = Column(
        Enum("DEV", "QA", "PROD", name="environment_enum"),
        nullable=True
    )

    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    max_users = Column(Integer, nullable=True)

    status = Column(
        Enum("ACTIVE", "EXPIRED", "SUSPENDED", name="status_enum"),
        nullable=True
    )

    created_at = Column(DateTime, server_default=func.now())