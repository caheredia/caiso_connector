import os
from starlette.testclient import TestClient
from src.helpers import TEST_DATABASE_LOCATION, get_db_location

os.environ["DATABASE_LOCATION"] = TEST_DATABASE_LOCATION  # isort:skip
from app.main import app  # isort:skip # noqa

client = TestClient(app)


def test_get_row_count():
    response = client.get("/row-count")
    assert response.status_code == 200
    assert isinstance(response.json().get("row-count"), int)


def test_get_time_ranges():
    response = client.get("/time-ranges")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_lmp_no_region():
    response = client.get("/lmp")
    assert response.status_code == 200
    assert isinstance(response.json().get("regions"), list)


def test_lmp_with_region():
    response = client.get("/lmp/AFPR_1_TOT_GEN-APND")
    assert response.status_code == 200
    assert isinstance(response.json()[0], dict)


def test_lmp_no_region_bad_response():
    response = client.get("/lmp/")
    assert response.status_code == 404


def test_lmp_mean():
    response = client.get("/lmp/mean/{region}/{day_of_week}")
    assert response.status_code == 422


def test_lmp_mean_with_node():
    response = client.get("/lmp/mean/AFPR_1_TOT_GEN-APND/monday")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_db_location():
    assert TEST_DATABASE_LOCATION == get_db_location()
