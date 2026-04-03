# Ecommerce Analytics Dashboard V2

## 🚀 Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy

## 📊 Data Model
Star Schema:
- dim_date
- dim_customer
- dim_product
- fact_sales

## ⚙️ Setup

pip install -r requirements.txt

uvicorn app.main:app --reload