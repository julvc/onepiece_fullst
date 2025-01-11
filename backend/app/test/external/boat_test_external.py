from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.boatRoutesExt.requests.get")
def test_get_boats(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/boats/en"))
    response = client.get("/api/boats/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_boat_one_value():
    response = client.get("/api/boats/en/search?name=Merry")
    assert response.status_code == 200
    
def test_search_boat_two_values():
    response = client.get("/api/boats/en/search?name=Merry&type=Pirate")
    assert response.status_code == 200
    
def test_boat_count():
    response = client.get("/api/boats/en/count")
    assert response.status_code == 200

def test_get_boat_by_id():
    response = client.get("/api/boats/en/1")
    assert response.status_code == 200

def test_get_boats_by_crew():
    response = client.get("/api/boats/en/crew/8")
    assert response.status_code == 200

# def test_get_boats_count_by_crew():
#     response = client.get("/api/boats/en/count/crew/8")
#     assert response.status_code == 200

# def test_get_boats_by_captain():
#     response = client.get("/api/boats/en/captain/8")
#     assert response.status_code == 200

# def test_get_boats_count_by_crew():
#     response = client.get("/api/boats/en/count/captain/8")
#     assert response.status_code == 200