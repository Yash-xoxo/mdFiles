import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
import os

# Dummy training dataset for MVP
# features: [monthly_avg_spend, income, savings_rate]
X = np.array([
    [40000, 80000, 0.2],
    [30000, 60000, 0.1],
    [50000, 120000, 0.3],
    [45000, 90000, 0.15]
])
y = np.array([42000, 31000, 48000, 43000])  # next month expenses

model = LinearRegression()
model.fit(X, y)

os.makedirs(os.path.dirname(__file__), exist_ok=True)
joblib.dump(model, os.path.join(os.path.dirname(__file__), "model.joblib"))
print("Trained model saved to model.joblib")
