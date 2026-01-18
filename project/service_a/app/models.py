from pydantic import BaseModel

class Result(BaseModel):
    image_url: str
    people_count: int
