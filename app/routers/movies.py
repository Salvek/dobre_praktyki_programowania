from fastapi import APIRouter
from app.utils.load_csv import load_csv
from app.models.movie import Movie

router = APIRouter(prefix="/movies")

@router.get("")
def get_movies():
    db = load_csv("database/movies.csv")
    result = []
    for row in db:
        m = Movie(row["movieId"], row["title"], row["genres"])
        result.append(m.__dict__)
    return result
