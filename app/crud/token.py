from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.models.user_token import UserToken
from app.core.security import ACCESS_TOKEN_EXPIRE_MINUTES


def store_user_token(db: Session, user_id: int, token: str):

    expiration_time = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Check if token already exists for this user
    existing_token = db.query(UserToken).filter(
        UserToken.user_id == user_id
    ).first()

    if existing_token:
        # Replace existing token
        existing_token.token = token
        existing_token.token_expiration_time = expiration_time
    else:
        # Create new token entry
        new_token = UserToken(
            user_id=user_id,
            token=token,
            token_expiration_time = expiration_time
        )
        db.add(new_token)

    db.commit()
