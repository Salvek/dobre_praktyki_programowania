import requests

SERVICE_A_URL = "http://service-a:8000/results"

def send_result(image_url: str, count: int):
    """
    Wysyła wynik detekcji do Serwisu A.
    """
    try:
        r = requests.post(SERVICE_A_URL, json={
            "image_url": image_url,
            "people_count": count
        }, timeout=5)
        r.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Failed to send result: {e}")
