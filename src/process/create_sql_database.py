import sqlite3

filename = "src/output/lmp.db"
conn = sqlite3.connect(filename)

conn.close()
print("database created: ", filename)
