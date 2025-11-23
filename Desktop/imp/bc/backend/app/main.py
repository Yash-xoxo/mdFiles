from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os, joblib
from . import models
from .schemas import TransactionCreate, PredictRequest
from sqlalchemy.orm import Session

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI FinCoach API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/transactions/", response_model=dict)
def create_transaction(tx: TransactionCreate, db: Session = Depends(get_db)):
    db_tx = models.Transaction(user_id=1, amount=tx.amount, category=tx.category)
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return {"id": db_tx.id, "amount": db_tx.amount, "category": db_tx.category}

@app.post("/predict_next_month")
def predict(p: PredictRequest):
    # simple example: load model.joblib and predict from user features
    model_path = "./app/ml/model.joblib"
    try:
        model = joblib.load(model_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Model not available, run training")
    # for MVP create dummy features [monthly_avg_spend, income, savings_rate]
    features = [[50000.0, 80000.0, 0.2]]  # replace with real feature extraction
    pred = model.predict(features)
    return {"next_month_expense": float(pred[0])}
