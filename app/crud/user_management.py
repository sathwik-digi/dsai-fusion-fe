from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.models.customer import Customer
from app.models.role import Role
from app.models.user_role import UserRole
from app.schemas.user_management import CreateUserRequest
from app.core.security import hash_password
from app.utils.code_generator import generate_customer_code

def create_account(
    db: Session,
    data: CreateUserRequest,
    creator_user: User
):
    """
    creator_user → extracted from JWT
    """

    creator_roles = [role.role_name for role in creator_user.roles]

    # -------------------------------------------------
    # 🔐 Authorization Rules
    # -------------------------------------------------

    # if "PROVIDER" not in creator_roles and "CUSTOMER" not in creator_roles:
    #     raise HTTPException(status_code=403, detail="Not authorized")

    if "CUSTOMER_ADMIN" in creator_roles and data.role == "SUPER_ADMIN":
        raise HTTPException(status_code=403, detail="Customer cannot create Provider")

    # -------------------------------------------------
    # 🔎 Duplicate Checks
    # -------------------------------------------------

    if db.query(User).filter(User.username == data.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")

    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    # -------------------------------------------------
    # 🔑 Hash Password
    # -------------------------------------------------

    hashed_password = hash_password(data.password)

    # -------------------------------------------------
    # 🎯 CASE 1: Creating PROVIDER
    # -------------------------------------------------

    if data.role == "SUPER_ADMIN":

        new_user = User(
            customer_id=None,
            first_name=data.first_name,
            last_name=data.last_name,
            username=data.username,
            password_hash=hashed_password,
            email=data.email,
            status="ACTIVE"
        )

        db.add(new_user)
        db.flush()

        admin_role = db.query(Role).filter(Role.role_name == "SUPER_ADMIN").first()
        if not admin_role:
            raise Exception("SUPER_ADMIN role not found")

        # Assign role to user
        user_role = UserRole(
            user_id=new_user.user_id,
            role_id=admin_role.role_id
        )

        db.add(user_role)
        db.commit()

        return {
            "user_id": new_user.user_id,
            "role": "SUPER_ADMIN",
            "customer_id": None,
            "message": "Provider created successfully"
        }

    # -------------------------------------------------
    # 🎯 CASE 2: Creating CUSTOMER
    # -------------------------------------------------

    if data.role == "CUSTOMER_ADMIN":

        # if not data.company_name or not data.company_email:
        #     raise HTTPException(status_code=400, detail="Company details required")

        # # Create customer
        # customer_code = generate_customer_code(db, data.company_name)

        # new_customer = Customer(
        #     customer_code=customer_code,
        #     customer_name=data.company_name,
        #     contact_email=data.company_email,
        #     contact_phone=data.phone,
        #     contact_address=data.address,
        #     status="ACTIVE"
        # )

        # db.add(new_customer)
        # db.flush()

        # Create admin user for customer
        new_user = User(
            customer_id = data.customer_id,
            first_name=data.first_name,
            last_name=data.last_name,
            username=data.username,
            password_hash=hashed_password,
            email=data.email,
            status="ACTIVE"
        )

        db.add(new_user)
        db.flush()

        customer_admin_role = db.query(Role).filter(Role.role_name == "CUSTOMER_ADMIN").first()
        if not customer_admin_role:
            raise Exception("CUSTOMER_ADMIN role not found")

        # Assign role to user
        user_role = UserRole(
            user_id=new_user.user_id,
            role_id=customer_admin_role.role_id
        )

        db.add(user_role)
        db.commit()

        return {
            "user_id": new_user.user_id,
            "role": "CUSTOMER_ADMIN",
            "customer_id": data.customer_id,
            "message": "Customer created successfully"
        }

    # -------------------------------------------------
    # 🎯 CASE 3: Creating USER
    # -------------------------------------------------

    if data.role == "END_USER":

        # If provider creating user → must pass customer_id
        if "SUPER_ADMIN" in creator_roles:
            if not data.customer_id:
                raise HTTPException(status_code=400, detail="customer_id required")

            target_customer_id = data.customer_id

        # If customer creating user → auto assign their customer_id
        else:
            target_customer_id = creator_user.customer_id

        new_user = User(
            customer_id=target_customer_id,
            first_name=data.first_name,
            last_name=data.last_name,
            username=data.username,
            password_hash=hashed_password,
            email=data.email,
            status="ACTIVE"
        )

        db.add(new_user)
        db.flush()

        customer_admin_role = db.query(Role).filter(Role.role_name == "END_USER").first()
        if not customer_admin_role:
            raise Exception("END_USER role not found")

        # Assign role to user
        user_role = UserRole(
            user_id=new_user.user_id,
            role_id=customer_admin_role.role_id
        )

        db.add(user_role)
        db.commit()

        return {
            "user_id": new_user.user_id,
            "role": "END_USER",
            "customer_id": target_customer_id,
            "message": "User created successfully"
        }

    raise HTTPException(status_code=400, detail="Invalid role")