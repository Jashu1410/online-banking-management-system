import sqlite3

class Database:
    def __init__(self, db_name="bank.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row

    def execute(self, query, params=(), commit=False):
        cur = self.conn.cursor()
        cur.execute(query, params)
        if commit:
            self.conn.commit()
        return cur

