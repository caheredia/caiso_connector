import zipfile
from urllib.request import urlretrieve
import os

BASE_URL = "http://oasis.caiso.com/oasisapi/SingleZip"
query_name = "?queryname=PRC_LMP"
time_range = "&startdatetime=20190201T00:00-0000&enddatetime=20190206T00:00-0000"
query_params = "&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6"
# build full caiso url
target_url = BASE_URL + query_name + time_range + query_params
ZIP_DIRECTORY = 'src/data'


def download_csv_file(data_url: str, directory_path: str):
    """Download csv file.

    Parameters
    ----------
    data_url : str
        source url for data
    directory_path : str
        location of saved zipped file
    """
    urlretrieve(data_url, directory_path + '/temp.zip')


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
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
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

    Parameters
    ----------
    search_directory : str
    """
    for temp_file in os.listdir(search_directory):
        os.remove(os.path.join(search_directory, temp_file))

# "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_INTVL_LMP&startdatetime=20190201T00:00-0000&enddatetime=20190206T00:00-0000&version=1&market_run_id=RTM&grp_type=ALL_APNODES&resultformat=6
# "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&startdatetime=20190201T00:00-0000&enddatetime=20190203T00:00-0000&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6
