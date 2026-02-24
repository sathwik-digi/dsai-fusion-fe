from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.customer import Customer
from app.models.user import User
from app.schemas.customer import CustomerCreate
from app.utils.code_generator import generate_customer_code
# from app.utils.id_generator import generate_user_id
from app.core.security import hash_password

from app.models.user import User
from app.models.customer import Customer
from app.models.user_role import UserRole
from app.models.role import Role
from fastapi import HTTPException


def register_customer(db: Session, data: CustomerCreate):

    # Check if username already exists
    existing_user = db.query(User).filter(User.username == data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Check if user email already exists
    existing_user_email = db.query(User).filter(User.email == data.user_email).first()
    if existing_user_email:
        raise HTTPException(status_code=400, detail="User email already exists")

    # Check if company email already exists
    existing_company_email = db.query(Customer).filter(Customer.contact_email == data.company_email).first()
    if existing_company_email:
        raise HTTPException(status_code=400, detail="Company email already exists")


    try:
        # 1️⃣ Create Customer (Company)
        customer_code = generate_customer_code(db, data.company_name)
        db_customer = Customer(
            customer_code=customer_code,
            customer_name=data.company_name,
            contact_email=data.company_email,
            contact_phone=data.phone,
            contact_address=data.address,
            status="INACTIVE"  # default as per requirement
        )

        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)

        # 2️⃣ Create Admin User for that Customer
        # new_user_id = generate_user_id(db, user_type="customer")
        hashed_password = hash_password(data.password)
        admin_user = User(
            # user_id=new_user_id,
            customer_id=db_customer.customer_id,
            first_name=data.first_name,
            last_name=data.last_name,
            username=data.username,
            password_hash=hashed_password,  # hash later
            email=data.user_email,
            status="INACTIVE"
        )

        db.add(admin_user)

        # 3️⃣ Commit
        db.commit()


        customer_admin_role = db.query(Role).filter(Role.role_name == "CUSTOMER_ADMIN").first()
        print(customer_admin_role.role_id,"idddd")
        if not customer_admin_role:
            raise Exception("CUSTOMER_ADMIN role not found")

        # Assign role to user
        user_role = UserRole(
            user_id=admin_user.user_id,
            role_id=customer_admin_role.role_id
        )

        db.add(user_role)
        db.commit()

        return db_customer


    except Exception as e:
        db.rollback()
        raise e

