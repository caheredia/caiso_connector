import os
import tempfile

from src.helpers import TEST_DATABASE_LOCATION, get_db_location, move_file

os.environ["DATABASE_LOCATION"] = TEST_DATABASE_LOCATION


def test_get_db_location():
    """
    Should return TEST_DATABASE_LOCATION location in test environment.
    """
    assert get_db_location() == TEST_DATABASE_LOCATION


def test_move_file():
    """
    Create a tempfile and move it with function
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = os.path.join(temp_dir, "temp_file.py")
        with open(temp_path, "w+"):
            pass
        assert os.path.isfile(temp_path) is True

        sub_dir = os.path.join(temp_dir, "sub_temp")
        os.mkdir(sub_dir)
        move_file(temp_path, sub_dir)

        new_path = os.path.join(sub_dir, "temp_file.py")
        assert os.path.isfile(new_path) is True
