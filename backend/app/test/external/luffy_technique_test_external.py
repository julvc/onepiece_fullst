from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.luffytechniqueRoutesExt.requests.get")
def test_get_luffytechniques(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/luffytechniques/en"))
    response = client.get("/api/luffytechniques/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_luffytechnique_one_value():
    response = client.get("/api/luffytechniques/en/search?name=Merry")
    assert response.status_code == 200
    
def test_search_luffytechnique_two_values():
    response = client.get("/api/luffytechniques/en/search?name=Merry&type=Pirate")
    assert response.status_code == 200
    
def test_luffytechnique_count():
    response = client.get("/api/luffytechniques/en/count")
    assert response.status_code == 200

def test_get_luffytechnique_by_id():
    response = client.get("/api/luffytechniques/en/6")
    assert response.status_code == 200