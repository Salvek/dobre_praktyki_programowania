from fastapi import FastAPI
from app.routers.movies import router as movies_router
from app.routers.links import router as links_router
from app.routers.ratings import router as ratings_router
from app.routers.tags import router as tags_router

app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "world"}

app.include_router(movies_router)
app.include_router(links_router)
app.include_router(ratings_router)
app.include_router(tags_router)
