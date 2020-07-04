from datetime import timedelta

import pandas as pd

from sql_app import models
from sql_app.database import engine
from src.caiso_connector import (
    download_csv_file,
    find_csv_files,
    unzip_csv,
)
from src.helpers import ZIP_DIRECTORY, generate_url

models.Base.metadata.create_all(bind=engine)


if __name__ == "__main__":

    # Extract
    for date in pd.date_range("2020-01-01", "2020-01-02"):
        start_time = date.isoformat()[:-3].replace("-", "")
        end_time = (date + timedelta(days=1)).isoformat()[:-3].replace("-", "")
        target = generate_url(start_time, end_time)
        # download_csv_file(target, ZIP_DIRECTORY)
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
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html#r689dfd12abe5-1
        # writes all rows at once
        df.to_sql("lmp", engine, if_exists="append", index=False)
