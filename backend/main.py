from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="E-Commerce Backend")


@app.get("/")
def root():
    return {
        "message": "Backend is running",
        "service": "FastAPI",
        "status": "healthy"
    }


@app.get("/api/products")
def products():
    return {
        "products": [
            {
                "id": 1,
                "name": "Laptop",
                "price": 65000
            },
            {
                "id": 2,
                "name": "Mobile",
                "price": 30000
            },
            {
                "id": 3,
                "name": "Keyboard",
                "price": 2500
            }
        ]
    }


@app.get("/api/health")
def health():
    return {
        "status": "UP",
        "time": datetime.utcnow().isoformat()
    }
