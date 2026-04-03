from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from datetime import datetime

class Sale:
    __tablename__ = "fact_sales"
    
    sale_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("dim_customer.customer_id"))
    product_id = Column(Integer, ForeignKey("dim_product.product_id"))
    date_id = Column(Integer, ForeignKey("dim_date.date_id"))
    quantity = Column(Integer, nullable=False)
    total_amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
