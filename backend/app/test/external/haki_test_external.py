from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.hakiRoutesExt.requests.get")
def test_get_hakis(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/hakis/en"))
    response = client.get("/api/hakis/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_haki_one_value():
    response = client.get("/api/hakis/en/search?name=Merry")
    assert response.status_code == 200
    
def test_search_haki_two_values():
    response = client.get("/api/hakis/en/search?name=Merry&type=Pirate")
    assert response.status_code == 200
    
def test_haki_count():
    response = client.get("/api/hakis/en/count")
    assert response.status_code == 200

def test_get_haki_by_id():
    response = client.get("/api/hakis/en/6")
    assert response.status_code == 200