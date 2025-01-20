from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.swordRoutesExt.requests.get")
def test_get_swords(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/swords/en"))
    response = client.get("/api/swords/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_sword_one_value():
    response = client.get("/api/swords/en/search?name=Merry")
    assert response.status_code == 200
    
def test_search_sword_two_values():
    response = client.get("/api/swords/en/search?name=Merry&type=Pirate")
    assert response.status_code == 200
    
def test_sword_count():
    response = client.get("/api/swords/en/count")
    assert response.status_code == 200

def test_get_sword_by_id():
    response = client.get("/api/swords/en/6")
    assert response.status_code == 200