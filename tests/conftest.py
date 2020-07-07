import pytest
from src.helpers import TEST_DATABASE_LOCATION


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    """Test for database location"""
    monkeypatch.setenv("DATABASE_LOCATION", TEST_DATABASE_LOCATION)
