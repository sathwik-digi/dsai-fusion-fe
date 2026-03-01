from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.v1 import auth, customer, user_management, roles, service_enablement, data_model, tool_integration, idp_config, fusion_config
from app.models import User, Customer, Role, FusionConfig, DataModel, UserRole, UserToken, ServiceEnablement, IdpConfig

Base.metadata.create_all( bind = engine )

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(customer.router, prefix="/api/v1/public/customers", tags=["Customer"])
app.include_router(user_management.router, prefix="/api/v1/addUsers", tags=["User Management"])
app.include_router(roles.router, prefix="/api/v1/roles", tags=["Roles"])
app.include_router(service_enablement.router,prefix="/api/v1/services",tags=["Service Enablement"])
app.include_router(data_model.router, prefix="/api/v1/data-models", tags=["Data Models"])
app.include_router(tool_integration.router,prefix="/api/v1/tools-integration",)
app.include_router(idp_config.router, prefix="/api/v1/idp-config", tags=["IDP Config"])
app.include_router(fusion_config.router,prefix="/api/v1/fusion-config",tags=["Fusion Config"])