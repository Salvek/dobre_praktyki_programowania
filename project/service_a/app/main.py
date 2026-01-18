from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Service A - Results")
app.include_router(router)
