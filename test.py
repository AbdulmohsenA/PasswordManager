from hashlib import sha256
import hashlib
import sqlite3
import dotenv
import os

#print(sha256("2".encode("utf-8")).hexdigest())

db = sqlite3.connect("test.db")

db.execute('''CREATE TABLE IF NOT EXISTS Passwords (
    Service varChar(255),
    Username varChar(255),
    Password varChar(255) NOT NULL
);''')

db.execute('''INSERT INTO Passwords (Service, Password)
VALUES ("this2", "adminpass123")''')


cursor = db.execute("SELECT * FROM Passwords")
db.commit()
print(cursor.fetchall())