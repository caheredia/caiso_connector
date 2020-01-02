from fastapi import FastAPI
import pandas as pd
import sqlite3
from json import loads
from enum import Enum
from src.helpers import DATABASE_LOCATION

app = FastAPI()

# Connect to database
conn = sqlite3.connect(DATABASE_LOCATION)


@app.get("/row-count")
async def get_row_count():
    count = pd.read_sql_query("""select COUNT(*) from lmp;""", conn).values[0][0]
    return {"row-count": int(count)}


@app.get("/time-ranges")
async def get_time_ranges():
    min_time = pd.read_sql_query("""select min(time) from lmp;""", conn).values[0][0]
    max_time = pd.read_sql_query("""select max(time) from lmp;""", conn).values[0][0]
    return {"oldest timestamp": min_time, "newest timestamp": max_time}


@app.get("/lmp")
async def get_lmp_regions():
    regions = pd.read_sql_query("""select distinct node from lmp;""", conn).values.tolist()
    return {"regions": regions}


@app.get("/lmp/{region}")
async def get_lmp_by_region(region: str):
    """Return the LMP for given region.
    For example region = "AFPR_1_TOT_GEN-APND"
    """
    data = pd.read_sql_query(
        f"""select * from lmp
        WHERE node == '{region}';
        """,
        conn).to_json(orient='records')
    return loads(data)


class DayOfWeek(str, Enum):
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    saturday = "saturday"
    sunday = "sunday"


@app.get("/lmp/mean/{region}/{day_of_week}")
async def get_mean_lmp_region_and_day_of_week(region: str, day_of_week=DayOfWeek):
    """Return the mean LMP for a given region and day of week.
    For example region = "AFPR_1_TOT_GEN-APND", day-of-week = "monday"
    """
    day_of_week_dict = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }
    day = day_of_week.value
    df_afpr = pd.read_sql_query("""select * from lmp WHERE node == "AFPR_1_TOT_GEN-APND";""", conn)
    df_afpr.time = pd.to_datetime(df_afpr.time)
    mean_lpm = df_afpr[df_afpr['time'].dt.dayofweek == day_of_week_dict.get(day)].mean()[0]
    mean_lpm = round(mean_lpm, 2)
    return {"region": region, "day-of-week": day, "mean_lpm": mean_lpm}
