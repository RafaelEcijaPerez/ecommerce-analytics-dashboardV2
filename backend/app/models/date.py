from sqlalchemy import Column, Integer, String, Date
from datetime import datetime

class Date:
    __tablename__ = "dim_date"
    
    date_id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, unique=True)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    day_of_week = Column(String(10))
