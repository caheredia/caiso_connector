from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_row_count():
    response = client.get("/row-count")
    assert response.status_code == 200
    assert isinstance(response.json().get('row-count'), int)


def test_get_time_ranges():
    response = client.get("/time-ranges")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_lmp_no_region():
    response = client.get("/lmp")
    assert response.status_code == 200
    assert isinstance(response.json().get('regions'), list)


def test_lmp_no_region():
    response = client.get("/lmp/")
    assert response.status_code == 404
