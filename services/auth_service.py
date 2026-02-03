import bcrypt
from database.db import Database

class AuthService:
    def __init__(self, db: Database):
        self.db = db

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, password, hashed):
        return bcrypt.checkpw(password.encode(), hashed)

    def register(self, username, password):
        hashed = self.hash_password(password)
        self.db.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, hashed),
            commit=True
        )

    def login(self, username, password):
        cur = self.db.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cur.fetchone()
        if user and self.verify_password(password, user["password_hash"]):
            return user
        return None
