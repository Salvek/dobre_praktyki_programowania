from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze():
    r = client.post("/analyze", json={
        "image_url": "http://example.com/img.jpg"
    })
    assert r.status_code == 200
