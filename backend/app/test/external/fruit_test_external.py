from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.fruitRoutesExt.requests.get")
def test_get_fruits(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/fruits/en"))
    response = client.get("/api/fruits/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_fruit_one_value():
    response = client.get("/api/fruits/en/search?name=Gum-Gum")
    assert response.status_code == 200
    
def test_search_fruit_two_values():
    response = client.get("/api/fruits/en/search?name=Fruit&type=Paramecia")
    assert response.status_code == 200
    
def test_fruit_count():
    response = client.get("/api/fruits/en/count")
    assert response.status_code == 200
    
def test_get_fruit_by_id():
    response = client.get("/api/fruits/en/1")
    assert response.status_code == 200
    
def test_get_fruit_count_by_search_one_value():
    response = client.get("/api/fruits/en/search/count?name=Gum-Gum")
    assert response.status_code == 200
    
def test_get_fruit_count_by_search_two_values():
    response = client.get("/api/fruits/en/search/count?name=Gum-Gum&type=Paramecia")
    assert response.status_code == 200 