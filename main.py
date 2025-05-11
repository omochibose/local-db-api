from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, OptaBi

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

# Create tables (no-op if already exists))

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/records")
def read_records(db: Session = Depends(get_db)):
    records = db.query(OptaBi).limit(100).all()
    return [r.__dict__ for r in records]