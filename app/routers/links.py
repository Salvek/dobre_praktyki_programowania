from fastapi import APIRouter
from app.utils.load_csv import load_csv
from app.models.link import Link

router = APIRouter(prefix="/links")

@router.get("")
def get_ratings():
    db = load_csv("database/link.csv")
    result = []
    for row in db:
        l = Link(row["movieId"], row["imdbId"], row["tmdbId"])
        result.append(l.__dict__)
    return result
