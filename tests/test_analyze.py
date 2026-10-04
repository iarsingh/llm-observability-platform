from fastapi.testclient import TestClient
from llmobs.main import app

client = TestClient(app)


def test_summary():
    payload = client.post("/analyze", json={"rows": [{'model': 'local-small', 'tokens': 40}, {'model': 'local-small', 'tokens': 120}, {'model': 'local-large', 'tokens': 80}]}).json()
    assert payload["mean"] == 80.0
    assert payload["by_model"]["local-small"]


def test_empty_is_refused():
    assert client.post("/analyze", json={"rows": []}).status_code == 422
