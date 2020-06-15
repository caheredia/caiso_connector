from fastapi import FastAPI, Depends
import pandas as pd
import sqlite3
from json import loads
from enum import Enum
from pydantic import BaseModel
from app import config

app = FastAPI()

# TODO fix this this in test_api
async def get_conn():
    return sqlite3.connect(config.settings.database)


@app.get("/row-count")
async def get_row_count(conn: sqlite3.Connection = Depends(get_conn)):
    count = pd.read_sql_query("""select COUNT(*) from lmp;""", conn).values[0][0]
    return {"row-count": int(count)}


@app.get("/time-ranges")
async def get_time_ranges(conn: sqlite3.Connection = Depends(get_conn)):
    min_time = pd.read_sql_query("""select min(time) from lmp;""", conn).values[0][0]
    max_time = pd.read_sql_query("""select max(time) from lmp;""", conn).values[0][0]
    return {"oldest timestamp": min_time, "newest timestamp": max_time}


@app.get("/lmp")
async def get_lmp_regions(conn: sqlite3.Connection = Depends(get_conn)):
    regions = pd.read_sql_query(
        """select distinct node from lmp;""", conn
    ).values.tolist()
    return {"regions": regions}


@app.get("/lmp/{region}")
async def get_lmp_by_region(region: str, conn: sqlite3.Connection = Depends(get_conn)):
    """Return the LMP for given region.
    For example region = "AFPR_1_TOT_GEN-APND"
    """
    data = pd.read_sql_query(
        f"""select * from lmp
        WHERE node == '{region}';
        """,
        conn,
    ).to_json(orient="records")
    return loads(data)


class DayOfWeek(str, Enum):
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    saturday = "saturday"
    sunday = "sunday"


class MeanLMP(BaseModel):
    region: str = "AFPR_1_TOT_GEN-APND"
    day: str = "sunday"
    mean_lmp: float = 33.35


day_of_week_dict = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}


@app.get("/lmp/mean/{region}/{day_of_week}", response_model=MeanLMP)
async def get_mean_lmp_region_and_day_of_week(
    region: str, day_of_week: DayOfWeek, conn: sqlite3.Connection = Depends(get_conn)
):
    """Return the mean LMP for a given region and day of week.
    For example region = "AFPR_1_TOT_GEN-APND", day-of-week = "monday"
    """

    df_afpr = pd.read_sql_query(f"""select * from lmp WHERE node == {region};""", conn)
    df_afpr.time = pd.to_datetime(df_afpr.time)
    mean_lmp = df_afpr[
        df_afpr["time"].dt.dayofweek == day_of_week_dict.get(day_of_week)
    ].mean()[0]
    mean_lmp = round(mean_lmp, 2)
    return {"region": region, "day": day_of_week, "mean_lmp": mean_lmp}
