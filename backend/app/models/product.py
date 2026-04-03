from sqlalchemy import Column, Integer, String, Float
from datetime import datetime

class Product:
    __tablename__ = "dim_product"
    
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False)
    category = Column(String(255))
    price = Column(Float, nullable=False)
