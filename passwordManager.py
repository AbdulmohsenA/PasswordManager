import sqlite3, os, sys, string, random
from hashlib import sha256
from dotenv import load_dotenv
from time import sleep

def main():

    # Load the Admin password from .env file
    load_dotenv("ADMIN_.env")
    ADMIN_PASSWORD = os.environ["DATABASE_PASSWORD"]


    login = input("Enter password: ")

    while login != ADMIN_PASSWORD:
        login = input("Wrong password, try again: ")
        if login == "q":
            sys.exit(1)

    # Create a database file and a data table if they don't exist
    global db
    db = sqlite3.connect("PASSWORDS.db")
    
    db.execute('''CREATE TABLE IF NOT EXISTS Passwords (
        Service varChar(255),
        Username varChar(255),
        Password varChar(255) NOT NULL
    );''')
    

    choice = userInterface()
    while choice != "q":
        if choice == "ap": 
            username = input("Enter username: ")
            service = input("Enter service: ")
            add_password(service, username)
            print("Done.\n")

        elif choice == "list":
            list_passwords()
            print()

        else:
            print("\n\nWrong choice, try again.\n")

        sleep(1)
        choice = userInterface()

def userInterface():
    print("*"*20)
    print("ap -> Add Password")
    print("list -> List all passwords")
    print("q to quit")
    print("*"*20)

    choice = input("Enter your choice: ").lower()

    return choice


def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(chars) for i in range(12))
    return password

def add_password(service, username):
    password = generate_password()

    command = f'''INSERT INTO Passwords (Service, Username, Password)
    VALUES ('{service}', '{username}', '{password}')'''
    db.execute(command)
    db.commit()

def list_passwords():
    cursor = db.execute(f"SELECT * FROM Passwords")
    db.commit()

    for row in cursor.fetchall():
        print(f"Service: {row[0]} Username: {row[1]} Password: {row[2]}")




if __name__ == "__main__":
    main()