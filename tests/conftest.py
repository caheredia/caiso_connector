import pandas as pd
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.helpers import TEST_DATABASE_LOCATION

# Default to using sqlite in memory for fast tests.
# Can be overridden by environment variable for testing in CI against other
# database engines
SQLALCHEMY_DATABASE_URL = TEST_DATABASE_LOCATION

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# old code
# @pytest.fixture(autouse=True)
# def env_setup(monkeypatch):
#     """Used for setting up test database"""
#     monkeypatch.setenv("DATABASE_LOCATION", TEST_DATABASE_LOCATION)


@pytest.fixture(scope="function")
def get_db():
    """
    Helper function, returns db sesion.
    """
    from sql_app.database import SessionLocal, engine
    from sql_app import models

    # establish models
    models.Base.metadata.create_all(bind=engine)

    # Seed Database for tests
    lmp_columns = ["INTERVALSTARTTIME_GMT", "NODE", "LMP_TYPE", "MW"]
    df = pd.read_csv(SEED_FILE, usecols=lmp_columns).rename(
        columns={"INTERVALSTARTTIME_GMT": "time", "NODE": "node", "MW": "mw"}
    )
    df.time = pd.to_datetime(df.time)
    df = df[df["LMP_TYPE"] == "LMP"].drop(columns=["LMP_TYPE"])
    # pandas can't be allowed to replace existing table, otherwise metadata is lost
    df.to_sql("lmp", engine, if_exists="append", index=False)
    return SessionLocal()
