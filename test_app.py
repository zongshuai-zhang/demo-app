from fastapi.testclient import TestClient
from app import app
import unittest

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["app"], "demo-app")

    def test_echo(self):
        response = self.client.post("/echo", json={"message": "hello world"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["echo"], "hello world")

    def test_echo_empty(self):
        response = self.client.post("/echo", json={"message": "   "})
        self.assertEqual(response.status_code, 400)

    def test_greet(self):
        response = self.client.post("/greet", json={"name": "Alice"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["greeting"], "Hello, Alice!")

    def test_greet_empty(self):
        response = self.client.post("/greet", json={"name": ""})
        self.assertEqual(response.status_code, 400)
