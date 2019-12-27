import zipfile
from urllib.request import urlretrieve
import pandas as pd
import os

base_url = "http://oasis.caiso.com/oasisapi/SingleZip"
query_name = "?queryname=PRC_INTVL_LMP"
time_range = "&startdatetime=20190201T08:00-0000&enddatetime=20190602T08:00-0000"
query_params = "&version=1&market_run_id=RTM&grp_type=ALL_APNODES&resultformat=6"
# build full caiso url
target_url = base_url + query_name + time_range + query_params

zip_file_path = 'data/temp.zip'
zip_directory = 'data'


def download_csv_file(data_url: str, file_path: str):
    """Download csv file.

    Parameters
    ----------
    data_url : str
        source url for data
    file_path : str
        location of saved zipped file
    """
    urlretrieve(data_url, file_path)


def unzip_csv(file_path: str):
    """unzip csv file.

    Parameters
    ----------
    file_path : str
        location of saved zipped file
    """
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall('data')


def find_csv_files(search_directory: str):
    """search directory for csv files.

    Parameters
    ----------
    search_directory : str

    Returns
    -------
    csv_files: list
        list of files that end in .csv
    """
    csv_files = []
    for csv_file in os.listdir(search_directory):
        if csv_file.endswith(".csv"):
            csv_files.append(os.path.join(search_directory, csv_file))
    return csv_files


download_csv_file(target_url, zip_file_path)
unzip_csv(zip_file_path)

for file in find_csv_files(zip_directory):
    df = pd.read_csv(file)
    print(df.head())
    print(df.columns)
