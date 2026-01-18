from typing import List
from app.models import Result

_DB: List[Result] = []

def save_result(result: Result):
    _DB.append(result)

def get_results():
    return _DB
