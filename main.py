from database.db import Database
from services.auth_service import AuthService
from services.bank_service import BankService
from services.transaction_service import TransactionService

db = Database()
auth = AuthService(db)
bank = BankService(db)
txn = TransactionService(db)

print("1. Register\n2. Login")
choice = input("Choose: ")

if choice == "1":
    u = input("Username: ")
    p = input("Password: ")
    auth.register(u, p)
    print("Registered successfully")

elif choice == "2":
    u = input("Username: ")
    p = input("Password: ")
    user = auth.login(u, p)
    if not user:
        print("Invalid login")
        exit()

    print("Login successful")

    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Exit")
        ch = input("Choose: ")

        if ch == "1":
            cid = input("Customer ID: ")
            atype = input("Account type: ")
            bank.create_account(cid, atype)
            print("Account created")

        elif ch == "2":
            acc = input("Account ID: ")
            amt = float(input("Amount: "))
            txn.deposit(acc, amt)
            print("Deposited")

        elif ch == "3":
            acc = input("Account ID: ")
            amt = float(input("Amount: "))
            txn.withdraw(acc, amt)
            print("Withdrawn")

        elif ch == "4":
            f = input("From Account: ")
            t = input("To Account: ")
            amt = float(input("Amount: "))
            txn.transfer(f, t, amt)
            print("Transferred")

        else:
            break
