from sqlalchemy import(JSON, Column,BigInteger,Integer,Boolean,ForeignKey, Numeric,String,DateTime, Text)
from sqlalchemy.sql import func
from app.db.database import Base


class fileUploadPolicies(Base):
    __tablename__="file_upload_policies"

    policy_id=Column(BigInteger,primary_key=True,auto_increment=True)
    customer_id=Column(BigInteger,ForeignKey("customers.customer_id"),nullable=True,index=True)
    policy_name = Column(String(255), nullable=True)
    policy_description = Column(Text, nullable=True)

    max_file_size_mb = Column(Integer, nullable=True)

    allowed_file_types = Column(JSON, nullable=True)
    blocked_file_types = Column(JSON, nullable=True)

    max_files_per_user_daily = Column(Integer, nullable=True)

    max_total_storage_gb = Column(Numeric(10, 2), nullable=True)

    require_virus_scan = Column(Boolean, nullable=True)
    is_active = Column(Boolean, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())