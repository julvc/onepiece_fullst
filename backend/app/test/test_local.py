from fastapi.testclient import TestClient
from app.main import app
from app.db import mongo

client = TestClient(app)

def test_create_read_item():
    item = {"name": "Test Saga"}
    response = client.post("/api/local/", json=item)
    assert response.status_code == 200
    item_id = response.json()["id"]

    get_response = client.get(f"/api/local/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Test Saga"