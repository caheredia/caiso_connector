import datetime
from sql_app import models
from sql_app.database import engine, SessionLocal
import pandas as pd

models.Base.metadata.create_all(bind=engine)
db = SessionLocal()
db_lmp = models.Lmp(time=datetime.datetime.now(), node="foo", mw=1.2)
db.add(db_lmp)
db.commit()
db.refresh(db_lmp)
# print(models.Base.metadata.tables)
# print(db.query(models.Lmp.node).all())
# TODO db query returns class objects, create new database from csv!
for user in db.query(models.Lmp)[0:3]:
    print(user.time)
    print(user.node)
    print(user.mw)
