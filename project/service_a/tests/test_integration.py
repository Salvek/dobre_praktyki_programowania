from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_save_and_get():
    r = client.post("/results", json={
        "image_url": "test.jpg",
        "people_count": 5
    })
    assert r.status_code == 200

    r = client.get("/results")
    assert len(r.json()) == 1
