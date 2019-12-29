import pandas as pd
import sqlite3
from datetime import timedelta

from src.input.caiso_connector import (
    download_csv_file,
    unzip_csv,
    delete_data_files,
    find_csv_files,
    ZIP_DIRECTORY,
    target_url
)

# Connect to database
conn = sqlite3.connect("src/output/lmp.db")

if __name__ == "__main__":
    # Extract
    for date in pd.date_range("2019-11-01", "2019-11-29"):
        start_time = date.isoformat()[:-3].replace('-', '')
        end_time = (date + timedelta(days=1)).isoformat()[:-3].replace('-', '')
        target = f"http://oasis.caiso.com/oasisapi/SingleZip?queryname=PRC_LMP&startdatetime={start_time}-0000&enddatetime={end_time}-0000&version=1&market_run_id=DAM&grp_type=ALL_APNODES&resultformat=6"
        download_csv_file(target, ZIP_DIRECTORY)
        unzip_csv(ZIP_DIRECTORY)

        # Transform
        lmp_columns = ['INTERVALSTARTTIME_GMT', 'NODE', 'LMP_TYPE', 'MW']
        file = find_csv_files(ZIP_DIRECTORY)[0]
        df = (pd.read_csv(file, usecols=lmp_columns)
              .rename(columns={'INTERVALSTARTTIME_GMT': 'time', 'NODE': 'node', 'MW': 'mw'}))
        df.time = pd.to_datetime(df.time)
        df = df[df["LMP_TYPE"] == "LMP"].drop(columns=['LMP_TYPE'])

        # Load
        print(f"adding {start_time}")
        df.to_sql("lmp", conn, if_exists="append", index=False)

        delete_data_files(ZIP_DIRECTORY)
