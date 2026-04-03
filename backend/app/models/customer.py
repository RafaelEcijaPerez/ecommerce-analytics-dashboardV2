from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Customer:
    __tablename__ = "dim_customer"
    
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
