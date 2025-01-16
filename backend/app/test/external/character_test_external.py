from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.characterRoutesExt.requests.get")
def test_get_characters(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/characters/en"))
    response = client.get("/api/characters/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_boat_character():
    response = client.get("/api/boats/en/search?name=Monkey")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Verifica que haya resultados

def test_search_boat_job():
    response = client.get("/api/boats/en/search?job=Nami%Arme")
    assert response.status_code == 200

def test_search_boat_bonus():
    response = client.get("/api/boats/en/search?bounty=94.000.000")
    assert response.status_code == 200

def test_search_boat_age():
    response = client.get("/api/boats/en/search?age=40")
    assert response.status_code == 200

def test_search_boat_size():
    response = client.get("/api/boats/en/search?size=301")
    assert response.status_code == 200

def test_search_boat_all_values():
    response = client.get("/api/boats/en/search?name=Merry")
    assert response.status_code == 200

def test_character_count():
    response = client.get("/api/characters/en/crew/10/count")
    assert response.status_code == 200

def test_get_character_by_id():
    response = client.get("/api/characters/en/1")
    assert response.status_code == 200

def test_get_characters_count_by_crew():
    response = client.get("/api/characters/en/crew/8")
    assert response.status_code == 200
