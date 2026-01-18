from fastapi import APIRouter
from app.models import Result
from app.storage import save_result, get_results

router = APIRouter()

@router.post("/results")
def add_result(result: Result):
    save_result(result)
    return {"status": "saved"}

@router.get("/results")
def list_results():
    return get_results()
