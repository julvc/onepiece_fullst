from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.dialRoutesExt.requests.get")
def test_get_dials(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/dials/en"))
    response = client.get("/api/dials/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_dial_one_value():
    response = client.get("/api/dials/en/search?name=Merry")
    assert response.status_code == 200
    
def test_search_dial_two_values():
    response = client.get("/api/dials/en/search?name=Merry&type=Pirate")
    assert response.status_code == 200
    
def test_dial_count():
    response = client.get("/api/dials/en/count")
    assert response.status_code == 200

def test_get_dial_by_id():
    response = client.get("/api/dials/en/6")
    assert response.status_code == 200
