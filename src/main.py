import pandas as pd
from src.input.caiso_connector import (
    download_csv_file,
    unzip_csv,
    delete_data_files,
    find_csv_files,
    ZIP_DIRECTORY,
    target_url
)

if __name__ == "__main__":
    download_csv_file(target_url, ZIP_DIRECTORY)
    unzip_csv(ZIP_DIRECTORY)

    for file in find_csv_files(ZIP_DIRECTORY):
        df = pd.read_csv(file)
        print(df.head())
    print(df.columns)

    delete_data_files(ZIP_DIRECTORY)
