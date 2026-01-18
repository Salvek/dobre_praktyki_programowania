from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Service B - AI API")
app.include_router(router)
