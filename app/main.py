from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.v1 import auth, customer, user_management, roles, service_enablement
from app.models import User, Customer, fusion_config

Base.metadata.create_all( bind = engine )

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(customer.router, prefix="/api/v1/public/customers", tags=["Customer"])
app.include_router(user_management.router, prefix="/api/v1/addUsers", tags=["User Management"])
app.include_router(roles.router, prefix="/api/v1/roles", tags=["Roles"])
app.include_router(service_enablement.router,prefix="/api/v1/services",tags=["Service Enablement"])