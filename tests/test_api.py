import pytest
from http import HTTPStatus
from fastapi.testclient import TestClient

from order_api.api import app


@pytest.fixture
def client():
    return TestClient(app)


def test_should_status_code_200_on_verify_helthcheck(client):
    response = client.get("/healthcheck")
    assert response.status_code == HTTPStatus.OK


def test_should_return_json_on_verify_helthcheck(client):
    response = client.get("/healthcheck")
    assert response.headers["Content-Type"] == "application/json"


def test_should_return_info_on_verify_helthcheck(client):
    response = client.get("/healthcheck")
    assert response.json() == {"status": "ok"}
