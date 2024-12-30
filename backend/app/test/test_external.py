from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_sagas():
    response = client.get("/api/external/sagas")
    assert response.status_code == 200

def test_get_characters():
    response = client.get("/api/external/characters")
    assert response.status_code == 200