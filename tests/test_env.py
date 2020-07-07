import os

from src.helpers import TEST_DATABASE_LOCATION


def test_db_env_variable():
    """
    Confirm database envionment variable set by pytest.
    """
    assert os.getenv("DATABASE_LOCATION") == TEST_DATABASE_LOCATION
