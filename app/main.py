from enum import Enum
from json import loads

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

from sql_app.database import engine

app = FastAPI()


@app.get("/row-count")
async def get_row_count():
    count = pd.read_sql_query("""select COUNT(*) from lmp;""", engine).values[0][0]
    return {"row-count": int(count)}


@app.get("/time-ranges")
async def get_time_ranges():
    min_time = pd.read_sql_query("""select min(time) from lmp;""", engine).values[0][0]
    max_time = pd.read_sql_query("""select max(time) from lmp;""", engine).values[0][0]
    return {"oldest timestamp": min_time, "newest timestamp": max_time}


@app.get("/lmp")
async def get_lmp_regions():
    regions = pd.read_sql_query(
        """select distinct node from lmp;""", engine
    ).values.tolist()
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
        engine,
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
async def get_mean_lmp_region_and_day_of_week(region: str, day_of_week: DayOfWeek):
    """Return the mean LMP for a given region and day of week.
    For example region = "AFPR_1_TOT_GEN-APND", day-of-week = "monday"
    """

    df_afpr = pd.read_sql_query(
        f"""select * from lmp WHERE node == '{region}';""", engine
    )
    df_afpr.time = pd.to_datetime(df_afpr.time)
    mean_lmp = df_afpr[
        df_afpr["time"].dt.dayofweek == day_of_week_dict.get(day_of_week)
    ].mean()[0]
    mean_lmp = round(mean_lmp, 2)
    return {"region": region, "day": day_of_week, "mean_lmp": 33.35}


# TODO fix mean_lmp for tests
