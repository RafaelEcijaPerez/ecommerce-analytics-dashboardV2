from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import sales

app = FastAPI(
    title="Ecommerce Analytics Dashboard API",
    description="API for ecommerce analytics and reporting",
    version="2.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(sales.router, prefix="/api/sales", tags=["sales"])

@app.get("/")
def read_root():
    return {"message": "Ecommerce Analytics Dashboard API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
