from fastapi import APIRouter
from app.utils.load_csv import load_csv
from app.models.tag import Tag

router = APIRouter(prefix="/tags")

@router.get("")
def get_ratings():
    db = load_csv("database/tags.csv")
    result = []
    for row in db:
        t = Tag(row["userId"], row["movieId"], row["tag"], row["timestamp"])
        result.append(t.__dict__)
    return result

