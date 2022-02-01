import os, sys, dotenv, getpass
from hashlib import sha256

## Note: this program will run for 1 time and will delete itself automatically, be careful

# Create ADMIN.env file
with open("ADMIN.env", "w") as f:
    pass

# Hash the password and secure it
def secure_pass(password):
    return sha256(password.encode()).hexdigest()

PASS = getpass.getpass("Enter your main password: ")
KEY = 'gcPZx4_U1Xtw8Zl0dCCJdY02FKejaMQ-8a40RbLnO0M='
dotenv.set_key("ADMIN.env", "DATABASE_PASSWORD", secure_pass(PASS))
dotenv.set_key("ADMIN.env", "KEY", KEY)
os.remove(sys.argv[0])