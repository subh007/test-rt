import requests
import pytest

BASE_URL = "http://localhost:30080"

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict():
    r = requests.get(f"{BASE_URL}/predict")
    assert r.status_code == 200
    assert "result" in r.json()
