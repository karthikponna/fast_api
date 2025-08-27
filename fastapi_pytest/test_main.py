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
