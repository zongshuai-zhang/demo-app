from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["app"] == "demo-app"


def test_echo():
    response = client.post("/echo", json={"message": "hello world"})
    assert response.status_code == 200
    assert response.json()["echo"] == "hello world"


def test_echo_empty():
    response = client.post("/echo", json={"message": "   "})
    assert response.status_code == 400


def test_greet():
    response = client.post("/greet", json={"name": "Alice"})
    assert response.status_code == 200
    assert response.json()["greeting"] == "Hello, Alice!"


def test_greet_empty():
    response = client.post("/greet", json={"name": ""})
    assert response.status_code == 400
