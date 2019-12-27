import zipfile
from urllib.request import urlretrieve

zip_file_path = 'data/temp.zip'
target_url = "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_INTVL_LMP&startdatetime=20190201T08:00-0000&enddatetime=20190602T08:00-0000&version=1&market_run_id=RTM&grp_type=ALL_APNODES&resultformat=6"
print(target_url)


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


download_csv_file(target_url, zip_file_path)
unzip_csv(zip_file_path)
