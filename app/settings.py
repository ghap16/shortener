import os

DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///./app/db.sqlite3")
