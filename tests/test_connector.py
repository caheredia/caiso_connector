"""The intentions of this test suite is to unit test the project code.
However, we are assuming `unit` in this context is at the module level.
We are testing the behavior of code not the implementation."""
import os
from src.caiso_connector import (
    ZIP_DIRECTORY,
    download_csv_file,
    unzip_csv,
    delete_data_files
)


def test_connector():
    """Test the download and deletion of a zip file."""
    # download files and unzip files
    test_url = "http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&startdatetime=20190201T00:00-0000&enddatetime=20190203T00:00-0000&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6"
    download_csv_file(test_url, ZIP_DIRECTORY)
    unzip_csv(ZIP_DIRECTORY)

    assert len(os.listdir(ZIP_DIRECTORY)) > 0

    delete_data_files(ZIP_DIRECTORY)
    assert len(os.listdir(ZIP_DIRECTORY)) == 0
