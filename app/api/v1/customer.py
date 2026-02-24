from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.customer import CustomerCreate, CustomerResponse
from app.crud.customer import register_customer
from app.db.session import get_db

router = APIRouter()


@router.post("/register", response_model=CustomerResponse)
def register_customer_api(customer: CustomerCreate, db: Session = Depends(get_db)):
    try:
        new_customer = register_customer(db, customer)
        return new_customer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
