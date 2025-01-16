from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.crewRoutesExt.requests.get")
def test_get_crews(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/crews/en"))
    response = client.get("/api/crews/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

def test_search_crew_name():
    response = client.get("/api/crews/en/search?name=Chapeau")
    assert response.status_code == 200
    
def test_search_crew_crew():
    response = client.get("/api/crews/en/search?status=assets")
    assert response.status_code == 200
    
def test_search_crew_two_values():
    response = client.get("/api/crews/en/search?name=The%On-Air%crew&status=assets")
    assert response.status_code == 200
    
def test_crew_count():
    response = client.get("/api/crews/en/count")
    assert response.status_code == 200
    data = response.json()
    assert "count" in data  # Verifica que la clave 'count' exista
    assert isinstance(data["count"], int)  # Verifica que el valor sea un número
    
def test_get_crew_by_id():
    response = client.get("/api/crews/en/1")
    assert response.status_code == 200
    
def test_get_crew_by_yonko():
    response = client.get("/api/crews/en/yonko")
    assert response.status_code in [200, 404]  # Si puede no encontrar datos
    
def test_crew_count_by_yonko():
    response = client.get("/api/crews/en/yonko/count")
    assert response.status_code == 200
    