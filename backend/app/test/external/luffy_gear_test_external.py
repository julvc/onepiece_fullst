from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.luffygearRoutesExt.requests.get")
def test_get_luffygears(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/luffygears/en"))
    response = client.get("/api/luffygears/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_luffygear_one_value():
    response = client.get("/api/luffygears/en/search?name=Merry")
    assert response.status_code == 200
    
def test_search_luffygear_two_values():
    response = client.get("/api/luffygears/en/search?name=Merry&type=Pirate")
    assert response.status_code == 200
    
def test_luffygear_count():
    response = client.get("/api/luffygears/en/count")
    assert response.status_code == 200

def test_get_luffygear_by_id():
    response = client.get("/api/luffygears/en/6")
    assert response.status_code == 200