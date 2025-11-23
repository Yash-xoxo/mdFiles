# The Things To Do In GitHub

 
[See simple Markdown Syntax](read.md)


[See Advanced Markdown Syntax](advance.md)


How to run everything locally (fast path)

Clone repo and place backend & mobile as above.

Start DB + backend:
```
docker-compose up --build
# or if running DB separately, start backend locally:
# cd backend
# pip install -r requirements.txt
# uvicorn app.main:app --reload
```

Train model (inside backend container or locally):
```
python backend/app/ml/train_model.py
# confirm backend/app/ml/model.joblib exists
```

Start Expo app:

```
cd mobile
npm install
npx expo start
```

Test endpoints:

POST http://localhost:8000/transactions/ with JSON {"amount":2000,"category":"food"}

POST http://localhost:8000/predict_next_month with {"user_id":1}