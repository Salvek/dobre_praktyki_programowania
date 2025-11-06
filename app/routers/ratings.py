from fastapi import APIRouter
from app.utils.load_csv import load_csv
from app.models.rating import Rating

router = APIRouter(prefix="/ratings")

@router.get("")
def get_ratings():
    db = load_csv("database/ratings.csv")
    result = []
    for row in db:
        r = Rating(row["userId"], row["movieId"], row["rating"], row["timestamp"])
        result.append(r.__dict__)
    return result
