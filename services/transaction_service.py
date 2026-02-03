class TransactionService:
    def __init__(self, db):
        self.db = db

    def deposit(self, account_id, amount):
        self.db.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, account_id),
            commit=True
        )
        print("Deposit successful")

    def withdraw(self, account_id, amount):
        self.db.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ? AND balance >= ?",
            (amount, account_id, amount),
            commit=True
        )
        print("Withdrawal successful")

    def transfer(self, from_acc, to_acc, amount):
        self.withdraw(from_acc, amount)
        self.deposit(to_acc, amount)
        print("Transfer successful")
