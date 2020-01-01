from fastapi import FastAPI
import pandas as pd
import sqlite3
from json import loads
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
