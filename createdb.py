import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "students.db")
con = sqlite3.connect(DB_PATH)
con.commit()