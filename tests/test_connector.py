"""The intentions of this test suite is to unit test the project code.
However, we are assuming `unit` in this context is at the module level.
We are testing the behavior of code not the implementation."""
import os

from src.caiso_connector import delete_data_files, download_csv_file, unzip_csv
from src.helpers import ZIP_DIRECTORY, generate_url


def _test_connector():
    """Test the download and deletion of a zip file.
    Only the __init__.py should be present.
    """
    # download files and unzip files
    test_url = "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&startdatetime=20190201T00:00-0000&enddatetime=20190202T00:00-0000&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6"
    download_csv_file(test_url, ZIP_DIRECTORY)
    unzip_csv(ZIP_DIRECTORY)

    assert len(os.listdir(ZIP_DIRECTORY)) > 1

    delete_data_files(ZIP_DIRECTORY)
    assert len(os.listdir(ZIP_DIRECTORY)) == 1


def test_generate_url():
    test_url = "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&startdatetime=2019-12-12-0000&enddatetime=2019-12-13-0000&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6"
    assert generate_url("2019-12-12", "2019-12-13") == test_url
