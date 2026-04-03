from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("")
def get_sales(db: Session = Depends(get_db)):
    """Get all sales"""
    return {"sales": []}

@router.get("/{sale_id}")
def get_sale(sale_id: int, db: Session = Depends(get_db)):
    """Get a specific sale by ID"""
    return {"sale_id": sale_id}

@router.post("")
def create_sale(db: Session = Depends(get_db)):
    """Create a new sale"""
    return {"message": "Sale created"}
