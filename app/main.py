from fastapi import FastAPI
import pandas as pd
import sqlite3

app = FastAPI()

# Connect to database
conn = sqlite3.connect("src/lmp.db")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/row-count")
async def get_row_count():
