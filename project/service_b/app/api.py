from fastapi import APIRouter
from app.rabbit import publish

router = APIRouter()

@router.post("/analyze")
def analyze(payload: dict):
    publish(payload)
    return {"status": "queued"}
