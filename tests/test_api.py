import os

import pandas as pd
from starlette.testclient import TestClient
from src.caiso_connector import find_csv_files
from src.helpers import (
    TEST_DATABASE_LOCATION,
    SEED_FILE,
)

os.environ["DATABASE_LOCATION"] = TEST_DATABASE_LOCATION  # isort:skip
from sql_app.database import engine  # isort:skip # noqa


# Seed Database for tests
lmp_columns = ["INTERVALSTARTTIME_GMT", "NODE", "LMP_TYPE", "MW"]
df = pd.read_csv(SEED_FILE, usecols=lmp_columns).rename(
    columns={"INTERVALSTARTTIME_GMT": "time", "NODE": "node", "MW": "mw"}
)
df.time = pd.to_datetime(df.time)
df = df[df["LMP_TYPE"] == "LMP"].drop(columns=["LMP_TYPE"])
df.to_sql("lmp", engine, if_exists="replace", index=False)

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
