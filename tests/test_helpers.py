import os

from src.helpers import get_db_location, TEST_DATABASE_LOCATION


os.environ["DATABASE_LOCATION"] = TEST_DATABASE_LOCATION


def test_get_db_location():
    """
    Should return TEST_DATABASE_LOCATION location in test environment.
    """
    assert get_db_location() == TEST_DATABASE_LOCATION
