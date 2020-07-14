from typing import Any, Generator

import pytest
from fastapi import FastAPI
from fastapi.applications.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.helpers import TEST_DATABASE_LOCATION
from sql_app.main import app
from sql_app.models import Base

# Default to using sqlite in memory for fast tests.
# Can be overridden by environment variable for testing in CI against other
# database engines
SQLALCHEMY_DATABASE_URL = TEST_DATABASE_LOCATION

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True)
def app_client() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    Base.metadata.create_all(engine)  # Create the tables.
    yield app
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(app: FastAPI) -> Generator[Session, Any, None]:
    """
    Creates a fresh sqlalchemy session for each test that operates in a
    transaction. The transaction is rolled back at the end of each test ensuring
    a clean state.
    """

    # connect to the database
    connection = engine.connect()
    # begin a non-ORM transaction
    transaction = connection.begin()
    # bind an individual Session to the connection
    session = Session(bind=connection)
    yield session  # use the session in tests.
    session.close()
    # rollback - everything that happened with the
    # Session above (including calls to commit())
    # is rolled back.
    transaction.rollback()
    # return connection to the Engine
    connection.close()


@pytest.fixture()
def client(app: FastAPI, db_session: Session) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into outes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client


# @pytest.fixture(scope="function")
# def get_db():
# """
# Helper function, returns db sesion.
# """
# from sql_app.database import SessionLocal, engine
# from sql_app import models

# # establish models
# models.Base.metadata.create_all(bind=engine)

# # Seed Database for tests
# lmp_columns = ["INTERVALSTARTTIME_GMT", "NODE", "LMP_TYPE", "MW"]
# df = pd.read_csv(SEED_FILE, usecols=lmp_columns).rename(
#     columns={"INTERVALSTARTTIME_GMT": "time", "NODE": "node", "MW": "mw"}
# )
# df.time = pd.to_datetime(df.time)
# df = df[df["LMP_TYPE"] == "LMP"].drop(columns=["LMP_TYPE"])
# # pandas can't be allowed to replace existing table, otherwise metadata is lost
# df.to_sql("lmp", engine, if_exists="append", index=False)
# return SessionLocal()
