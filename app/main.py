from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Market Data API", version="1.0")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Market Data API Running"}