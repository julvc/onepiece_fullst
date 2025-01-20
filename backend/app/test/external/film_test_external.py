from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.filmRoutesExt.requests.get")
def test_get_movies(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/movies/en"))
    response = client.get("/api/movies/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_film_one_value():
    response = client.get("/api/movies/en/search?title=luffy")
    assert response.status_code == 200
    
def test_film_count():
    response = client.get("/api/movies/en/count")
    assert response.status_code == 200
    
def test_get_film_by_id():
    response = client.get("/api/movies/en/1")
    assert response.status_code == 200
    
def test_get_count_movies_by_search():
    response = client.get("/api/movies/en/search/count?title=Gum-Gum")
    assert response.status_code == 200
