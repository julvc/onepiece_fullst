from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.sagasRoutesExt.requests.get")
def test_get_sagas(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/sagas/en"))
    response = client.get("/api/sagas/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_saga():
    response = client.get("/api/sagas/en/search?title=Alabasta")
    assert response.status_code == 200

def test_get_saga_count():
    response = client.get("/api/sagas/en/count")
    assert response.status_code == 200

def test_get_saga_by_id():
    response = client.get("/api/sagas/en/1")
    assert response.status_code == 200
