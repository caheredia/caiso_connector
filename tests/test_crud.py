from sql_app.crud import get_lmps, get_row_count
from src.helpers import SEED_FILE
import pandas as pd


def get_db():
    """
    Helper function, returns db sesion.
    """
    from sql_app.database import SessionLocal, engine
    from sql_app import models

    # establish models
    models.Base.metadata.create_all(bind=engine)

    # Seed Database for tests
    lmp_columns = ["INTERVALSTARTTIME_GMT", "NODE", "LMP_TYPE", "MW"]
    df = pd.read_csv(SEED_FILE, usecols=lmp_columns).rename(
        columns={"INTERVALSTARTTIME_GMT": "time", "NODE": "node", "MW": "mw"}
    )
    df.time = pd.to_datetime(df.time)
    df = df[df["LMP_TYPE"] == "LMP"].drop(columns=["LMP_TYPE"])
    # pandas can't be allowed to replace existing table, otherwise metadata is lost
    df.to_sql("lmp", engine, if_exists="append", index=False)
    return SessionLocal()


def test_lmps():
    """
    Test lmp crud function
    """
    breakpoint()
    db = get_db()
    lmps = get_lmps(db=db)
    assert isinstance(lmps, list)


def test_row_count():
    """
    Test row count
    """
    db = get_db()
    rows = get_row_count(db=db)
    assert isinstance(rows, int)
    assert rows == 9

