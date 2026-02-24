from sqlalchemy.orm import Session
from app.models.user import User


def generate_user_id(db: Session, user_type: str) -> str:

    if user_type.lower() == "provider":
        prefix = "PROV"
        base_number = 10000

    elif user_type.lower() == "customer":
        prefix = "CUST"
        base_number = 20000

    else:
        prefix = "USER"
        base_number = 30000

    # Fetch last user with this prefix
    last_user = (
        db.query(User)
        .filter(User.user_id.like(f"{prefix}-%"))
        .order_by(User.user_id.desc())
        .first()
    )

    if last_user:
        # Extract numeric part
        last_number = int(last_user.user_id.split("-")[1])
        new_number = last_number + 1
    else:
        new_number = base_number + 1

    return f"{prefix}-{new_number}"
