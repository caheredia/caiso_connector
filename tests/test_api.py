from starlette.testclient import TestClient
from app import config
from app import main

client = TestClient(main.app)


def get_settings_override():
    return config.Settings(database="tests/test_lmp.db")


main.app.dependency_overrides[main.get_conn] = get_settings_override


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


def test_lmp_no_region_bad_response():
    response = client.get("/lmp/")
    assert response.status_code == 404


def test_lmp_mean():
    response = client.get("/lmp/mean/{region}/{day_of_week}")
    assert response.status_code == 422
