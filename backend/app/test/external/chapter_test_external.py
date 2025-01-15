from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)


@patch("app.routes.external.chapterRoutesExt.requests.get")
def test_get_chapters(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/chapters/en"))
    response = client.get("/api/chapters/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_chapter_one_value():
    response = client.get("/api/chapters/en/search?title=Arc")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Verifica que haya resultados
    for chapter in response.json():
        print("Chapter:", chapter)  # Agrega esta línea para depuración
        assert "_id" in chapter  # Asegúrate de que 'id' esté presente, no '_id'
        assert "title" in chapter

def test_search_chapter_not_found():
    response = client.get("/api/chapters/en/search?title=Merry")
    print("Respuesta:", response.json())  # Depuración adicional
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()  # Verifica que el mensaje contenga "not found"

def test_chapter_count():
    response = client.get("/api/chapters/en/count")
    assert response.status_code == 200

def test_get_chapter_by_id():
    response = client.get("/api/chapters/en/1")
    assert response.status_code == 200

def test_get_chapters_by_tome():
    response = client.get("/api/chapters/en/tome/8")
    assert response.status_code == 200

def test_get_chapters_count_by_crew():
    response = client.get("/api/chapters/en/tome/8/count")
    assert response.status_code == 200
