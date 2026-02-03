from database.db import Database

class BankService:
    def __init__(self, db: Database):
        self.db = db

    def create_customer(self, name, email, phone, user_id):
        self.db.execute(
            "INSERT INTO customers (name, email, phone, user_id) VALUES (?, ?, ?, ?)",
            (name, email, phone, user_id),
            commit=True
        )

    def create_account(self, customer_id, account_type):
        self.db.execute(
            "INSERT INTO accounts (customer_id, account_type, balance) VALUES (?, ?, ?)",
            (customer_id, account_type, 0),
            commit=True
        )

    def get_account(self, account_id):
        cur = self.db.execute("SELECT * FROM accounts WHERE account_id = ?", (account_id,))
        return cur.fetchone()
