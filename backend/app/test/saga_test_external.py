from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_sagas():
    response = client.get("/api/external/sagas")
    assert response.status_code == 200

def test_get_saga_by_id():
    response = client.get("/api/external/sagas/1")
    assert response.status_code == 200

def test_search_saga():
    response = client.get("/api/external/sagas/search?title=Alabasta")
    assert response.status_code == 200

def test_get_saga_count():
    response = client.get("/api/external/sagas/count")
    assert response.status_code == 200