import sqlite3
from datetime import timedelta

import pandas as pd

from src.caiso_connector import (
    delete_data_files,
    download_csv_file,
    find_csv_files,
    unzip_csv,
)
from src.helpers import DATABASE_LOCATION, ZIP_DIRECTORY, generate_url

if __name__ == "__main__":
    # Connect to database
    conn = sqlite3.connect(DATABASE_LOCATION)

    # Extract
    for date in pd.date_range("2020-01-01", "2020-01-01"):
        start_time = date.isoformat()[:-3].replace("-", "")
        end_time = (date + timedelta(days=1)).isoformat()[:-3].replace("-", "")
        target = generate_url(start_time, end_time)
        download_csv_file(target, ZIP_DIRECTORY)
        unzip_csv(ZIP_DIRECTORY)

        # Transform
        lmp_columns = ["INTERVALSTARTTIME_GMT", "NODE", "LMP_TYPE", "MW"]
        file = find_csv_files(ZIP_DIRECTORY)[0]
        df = pd.read_csv(file, usecols=lmp_columns).rename(
            columns={"INTERVALSTARTTIME_GMT": "time", "NODE": "node", "MW": "mw"}
        )
        df.time = pd.to_datetime(df.time)
        df = df[df["LMP_TYPE"] == "LMP"].drop(columns=["LMP_TYPE"])

        # Load
        print(f"adding {start_time}")
        df.to_sql("lmp", conn, if_exists="append", index=False)

        delete_data_files(ZIP_DIRECTORY)
