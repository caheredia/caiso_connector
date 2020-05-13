from starlette.testclient import TestClient
from app.main import app
from hypothesis import given
import hypothesis.strategies as strategy

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


def test_lmp_no_region_bad_response():
    response = client.get("/lmp/")
    assert response.status_code == 404


def test_lmp_mean():
    response = client.get("/lmp/mean/{region}/{day_of_week}")
    assert response.status_code == 422

def add_int(x,y):
    return x + abs(y)

@given(strategy.integers(), strategy.integers())
def test_add(x, y ):
    assert add_int(x, y) == x + y

