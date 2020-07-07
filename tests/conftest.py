import pytest
from src.helpers import TEST_DATABASE_LOCATION


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    """Used for setting up test database"""
    monkeypatch.setenv("DATABASE_LOCATION", TEST_DATABASE_LOCATION)
