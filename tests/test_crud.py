import os

import pandas as pd
from starlette.testclient import TestClient
from src.helpers import TEST_DATABASE_LOCATION, SEED_FILE
from sql_app import models
from sql_app.crud import get_lmps

# set test db env variable
os.environ["DATABASE_LOCATION"] = TEST_DATABASE_LOCATION  # isort:skip
from sql_app.database import SessionLocal, engine  # isort:skip # noqa

# Seed Database for tests
lmp_columns = ["INTERVALSTARTTIME_GMT", "NODE", "LMP_TYPE", "MW"]
df = pd.read_csv(SEED_FILE, usecols=lmp_columns).rename(
    columns={"INTERVALSTARTTIME_GMT": "time", "NODE": "node", "MW": "mw"}
)
df.time = pd.to_datetime(df.time)
df = df[df["LMP_TYPE"] == "LMP"].drop(columns=["LMP_TYPE"])
# pandas can't be allowed to replace existing table, otherwise metadata is lost
df.to_sql("lmp", engine, if_exists="append", index=False)


# establish models
models.Base.metadata.create_all(bind=engine)
# start session
db = SessionLocal()


def test_lmps():
    """
    Test lmp crud function
    """
    lmps = get_lmps(db=db)
    assert isinstance(lmps, list)
