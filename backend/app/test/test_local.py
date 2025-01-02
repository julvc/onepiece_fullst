import pytest
# from httpx import AsyncClient
from fastapi.testclient import TestClient
from app.main import app
from app.utils.populate import populate_sagas


client = TestClient(app)  # Crea una instancia de TestClient pasando la app FastAPI

@pytest.mark.asyncio
async def test_get_sagas():
    await populate_sagas()
    response = client.get("/api/sagas")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_saga():
    payload = {
        "title": "Romance Dawn TESTING",
        "saga_number": "1001",
        "saga_chapitre": "1",
        "saga_volume": "3",
        "saga_episode": "15"
    }
    # async with AsyncClient(app=app) as ac:
    #     response = await ac.post("/api/sagas", json=payload)
    response = client.post("/api/sagas", json=payload) 
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert "id" in data

@pytest.mark.asyncio
async def test_get_saga_by_id():
    # Crea un nuevo registro primero
    payload = {
        "title": "Romance Dawn TESTING Two",
        "saga_number": "101",
        "saga_chapitre": "15",
        "saga_volume": "5",
        "saga_episode": "716"
    }
    
    # async with AsyncClient(app=app) as ac:
    #     create_response = await ac.post("/api/sagas", json=payload)
    #     saga_id = create_response.json()["id"]
    create_response = client.post("/api/sagas", json=payload)
    saga_id = create_response.json()["id"]

    # Consulta por ID
    get_response = client.get(f"/api/sagas/{saga_id}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == payload["title"]

@pytest.mark.asyncio
async def test_delete_saga():
    # Crea un nuevo registro
    payload = {
        "title": "Romance Dawn TESTING Three",
        "saga_number": "7",
        "saga_chapitre": "6",
        "saga_volume": "5",
        "saga_episode": "4"
    }
    # async with AsyncClient(app=app) as ac:
    #     create_response = await ac.post("/api/sagas", json=payload)
    #     saga_id = create_response.json()["id"]

    #     # Eliminar registro
    #     delete_response = await ac.delete(f"/api/sagas/{saga_id}")
    # assert delete_response.status_code == 200

    #     # Verificar que ya no existe
    # get_response = await ac.get(f"/api/sagas/{saga_id}")
    # assert get_response.status_code == 404
    create_response = client.post("/api/sagas", json=payload)
    saga_id = create_response.json()["id"]

    delete_response = client.delete(f"/api/sagas/{saga_id}")
    assert delete_response.status_code == 200

    # Verificar que ya no existe
    get_response = client.get(f"/api/sagas/{saga_id}")
    assert get_response.status_code == 404