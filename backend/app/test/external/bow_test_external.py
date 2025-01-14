from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch("app.routes.external.bowRoutesExt.requests.get")
def test_get_arcs(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "mocked_data"}
    print("url")
    print(client.get("/api/arcs/en"))
    response = client.get("/api/arcs/en")
    assert response.status_code == 200
    assert response.json() == {"data": "mocked_data"}

# POSEE UN PROBLEMA LA API EXTERNA, SE ENVIO CORREO PARA REVISION
# def test_search_bow_one_value():
#     response = client.get("/api/arcs/en/search?title=Merry")
#     assert response.status_code == 200
    
def test_bow_count():
    response = client.get("/api/arcs/en/count")
    assert response.status_code == 200

def test_get_bow_by_id():
    response = client.get("/api/arcs/en/1")
    assert response.status_code == 200

def test_get_arcs_by_saga():
    response = client.get("/api/arcs/en/saga/8")
    assert response.status_code == 200

def test_get_arcs_count_by_saga():
    response = client.get("/api/arcs/en/count/saga/8")
    assert response.status_code == 200