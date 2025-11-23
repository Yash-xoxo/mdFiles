from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionCreate(BaseModel):
    amount: float
    category: str

class TransactionOut(TransactionCreate):
    id: int
    created_at: datetime

class PredictRequest(BaseModel):
    user_id: int
