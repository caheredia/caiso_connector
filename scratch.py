# TODO set this up staring with establishing a memeory sql database then use crud methods
import datetime
import os

from sql_app.crud import get_row_count
import pandas as pd
from src.helpers import TEST_DATABASE_LOCATION, SEED_FILE

# set test db env variable
os.environ["DATABASE_LOCATION"] = TEST_DATABASE_LOCATION  # isort:skip
from sql_app.database import SessionLocal, engine  # isort:skip # noqa

from sql_app import models

# establish models
models.Base.metadata.create_all(bind=engine)
# start session
db = SessionLocal()

db_lmp = models.Lmp(time=datetime.datetime.now(), node="foo", mw=1.2)
db.add(db_lmp)
db.commit()
db.refresh(db_lmp)
print(models.Base.metadata.tables)
print(db.query(models.Lmp.node).all())
print(db.execute("SELECT * FROM lmp").fetchall())

# Seed Database for tests
lmp_columns = ["INTERVALSTARTTIME_GMT", "NODE", "LMP_TYPE", "MW"]
df = pd.read_csv(SEED_FILE, usecols=lmp_columns).rename(
    columns={"INTERVALSTARTTIME_GMT": "time", "NODE": "node", "MW": "mw"}
)
df.time = pd.to_datetime(df.time)
df = df[df["LMP_TYPE"] == "LMP"].drop(columns=["LMP_TYPE"])
# pandas can't be allowed to replace existing table, otherwise metadata is lost
df.to_sql("lmp", engine, if_exists="append", index=False)

breakpoint()
for user in db.query(models.Lmp):
    print(user.time)
    print(user.node)
    print(user.mw)

print(db.execute("SELECT COUNT(*) FROM lmp").fetchall())
print(get_row_count(db=db))


