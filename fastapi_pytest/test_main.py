from fastapi.testclient import TestClient
from .pytest_main import app, todos

client = TestClient(app)

# deleting the todos for every test 
def setup_function():
    todos.clear()

def test_read_todos():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_todo():
    response = client.post("/", json={"name": "Buy something", "completed": False})
    assert response.status_code == 200
    assert response.json() == {"name": "Buy something", "completed": False}

def test_read_todo():
    client.post("/", json={"name": "Buy something", "completed": False})
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Buy something", "completed": False}

def test_update_todo():
    client.post("/", json={"name": "Buy something", "completed": False})
    response = client.put("/1", json= {"name": "Buy something", "completed": True})
    assert response.status_code == 200
    assert response.json() == {"name": "Buy something", "completed": True}

def test_delete_todo():
    client.post("/", json={"name": "Buy something", "completed": False})
    response = client.delete("/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Buy something", "completed": False}
