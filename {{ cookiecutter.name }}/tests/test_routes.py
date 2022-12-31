from ..app import app
from fastapi.testclient import TestClient


cli = TestClient(app)


def test_initial():
    resp = cli.get("/")
    resp.status_code == 200
