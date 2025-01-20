from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.episodeRoutesExt.requests.get")
def test_get_episodes(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/episodes/en"))
    response = client.get("/api/episodes/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_episode_one_value():
    response = client.get("/api/episodes/en/search?title=Merry")
    assert response.status_code == 200
    
def test_episode_count():
    response = client.get("/api/episodes/en/count")
    assert response.status_code == 200

def test_get_episode_by_id():
    response = client.get("/api/episodes/en/6")
    assert response.status_code == 200
    
def test_get_count_episodes_by_saga():
    response = client.get("/api/episodes/en/count/saga/9")
    assert response.status_code == 200
    
def test_get_count_episodes_by_arc():
    response = client.get("/api/episodes/en/count/arc/2")
    assert response.status_code == 200
    
def test_search_episodes_by_saga():
    response = client.get("/api/episodes/en/search/saga?title=luffy")
    assert response.status_code == 200

def test_search_episodes_by_saga_id():
    response = client.get("/api/episodes/en/saga/9")
    assert response.status_code == 200
    
# def test_search_episodes_by_arc():
#     response = client.get("/api/episodes/en/search/arc?title=Arc%Romance%Dawn")
#     assert response.status_code == 200

def test_search_episodes_by_arc_id():
    response = client.get("/api/episodes/en/arc/9")
    assert response.status_code == 200