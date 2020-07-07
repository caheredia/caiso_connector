import os
import zipfile
from urllib import request

DATABASE_LOCATION = "sqlite:///src/lmp.db"
TEST_DATABASE_LOCATION = "sqlite:///:memory:"
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


def download_csv_file(data_url: str, directory_path: str):
    """Download csv file.

    Parameters
    ----------
    data_url : str
        source url for data
    directory_path : str
        location of saved zipped file
    """
    request.urlretrieve(data_url, directory_path + "/temp.zip")


def unzip_csv(directory_path: str):
    """unzip csv files.

    Parameters
    ----------
    directory_path : str
        location of saved zipped file
    """

    for zip_file in os.listdir(directory_path):
        if zip_file.endswith(".zip"):
            zip_path = os.path.join(directory_path, zip_file)
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(directory_path)


def find_csv_files(directory_path: str):
    """search directory for csv files.

    Parameters
    ----------
    directory_path : str

    Returns
    -------
    csv_files: list
        list of files that end in .csv
    """
    csv_files = []
    for csv_file in os.listdir(directory_path):
        if csv_file.endswith(".csv"):
            csv_files.append(os.path.join(directory_path, csv_file))
    return csv_files


def delete_data_files(search_directory: str):
    """Deletes the contents of download directory.
    If file has .zip for or .csv extension

    Parameters
    ----------
    search_directory : str
    """
    for temp_file in os.listdir(search_directory):
        if temp_file.endswith(".csv") or temp_file.endswith(".zip"):
            os.remove(os.path.join(search_directory, temp_file))
