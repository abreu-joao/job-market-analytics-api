from fastapi import FastAPI
from app.database import engine, Base
from app.api.routes import jobs_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Market API")

@app.get("/")
def home():
    return {"status": "online", "message": "Job Market API is running"}

@app.get("/health", tags=["Infrastructure"])
def health_check():
    return {"status": "online", "database": "connected"}

app.include_router(jobs_router)