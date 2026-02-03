import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "bank.db"
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

with open(SCHEMA_PATH, "r") as f:
    cur.executescript(f.read())

conn.commit()
conn.close()

print("Database initialized successfully")
