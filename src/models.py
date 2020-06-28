import sqlalchemy as db

engine = db.create_engine("sqlite:///lmp.db")
connection = engine.connect()
metadata = db.MetaData()
lmp = db.Table("lmp", metadata, autoload=True, autoload_with=engine)


# class Lmp(db.Model):
#     time = db.Column(db.TIMESTAMP(), nullable=False)
#     node = db.Column(db.Text(), nullable=False)
#     mw = db.Column(db.REAL(), nullable=False)

#     def __repr__(self):
#         return f"Lmp('{self.time}', '{self.node}', '{self.mw}')"


# print columns
print(lmp.columns.keys())

# Print full table metadata
print(repr(metadata.tables["lmp"]))

# print node column
query = db.select([lmp])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet[0:10])

# Table('lmp', MetaData(bind=None), Column('time', TIMESTAMP(), table=<lmp>), Column('node', TEXT(), table=<lmp>), Column('mw', REAL(), table=<lmp>), schema=None)
