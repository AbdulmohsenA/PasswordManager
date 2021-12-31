import sqlite3, os
from hashlib import sha256
from dotenv import load_dotenv
import sys

# Load the Admin password from .env file
load_dotenv("ADMIN_.env")
ADMIN_PASSWORD = os.environ["DATABASE_PASSWORD"]


login = input("Enter password: ")

while login != ADMIN_PASSWORD:
    login = input("Wrong password, try again: ")
    if login == "q":
        sys.exit(1)

# Create a database file and a data table if they don't exist
db = sqlite3.connect("PASSWORDS.db")

db.execute('''CREATE TABLE IF NOT EXISTS Passwords (
    Service varChar(255),
    Username varChar(255),
    Password varChar(255) NOT NULL
);''')

#TODO Add main functions (Add pass, get pass, list passwords, etc..)
#TODO make main function


