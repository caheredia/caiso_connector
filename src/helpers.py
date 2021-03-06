import os

DATABASE_LOCATION = "sqlite:///src/lmp.db"
TEST_DATABASE_LOCATION = "sqlite:///tests/test_lmp.db"
ZIP_DIRECTORY = "src/temp_data"
SEED_FILE = "src/data/seed.csv"
DATA_DIR = "src/data"


def get_db_location() -> str:
    """Set the database location.
    If the environment variable isn't set then use default.
    """
    location = os.getenv("DATABASE_LOCATION")
    if location:
        return location
    else:
        return DATABASE_LOCATION


def generate_url(start_time: str, end_time: str) -> str:
    """Generates a CAISO OASIS url based on start and time.

    Parameters
    ----------
    start_time : str
        start timestamp
    end_time : str
        end timestamp

    Returns
    -------
    target_url: str
        OASIS url for download
    """

    base_url = "http://oasis.caiso.com/oasisapi/SingleZip"
    query = "?queryname=PRC_LMP"
    time_range = f"&startdatetime={start_time}-0000&enddatetime={end_time}-0000"
    version = "&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6"

    target_url = base_url + query + time_range + version
    return target_url


def move_file(file_path: str, new_directory: str = DATA_DIR) -> None:
    """
    Move file into desired directory.

    Parameters
    ----------
    file_path :
        relative or absolute file path
    new_directory :
        target directory for move
    """
    file_name = os.path.split(file_path)[-1]
    new_path = os.path.join(new_directory, file_name)
    os.rename(file_path, new_path)
