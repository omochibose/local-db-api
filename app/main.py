from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.database import SessionLocal, engine
from app.models import Base, OptaBi
from app.routes import filters
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS for google colab or local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Include filter routes
app.include_router(filters.router)

@app.get("/records")
def read_records(request: Request,db: Session = Depends(get_db)):
    """
    Retrieve records from the opta_bi table using query parameters as filters.
    Example: /records?teamName=Japan&season=2024
    """
    query_params = dict(request.query_params)
    filters = []

    for key, value in query_params.items():
        if hasattr(OptaBi, key):
            filters.append(getattr(OptaBi, key) == value)

    query = db.query(OptaBi)
    if filters:
        query = query.filter(and_(*filters))

    def to_dict(obj):
        return {k: v for k, v in obj.__dict__.items() if not k.startswith("_")}
    
    return [to_dict(row) for row in query.all()]