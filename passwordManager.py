import sqlite3, os, sys, string, random
from dotenv import load_dotenv
from time import sleep
from cryptography.fernet import Fernet

def main():

    # Load the Admin password from .env file
    load_dotenv("ADMIN.env")
    ADMIN_PASSWORD = os.environ["DATABASE_PASSWORD"]


    login = input("Enter password: ")

    while login != ADMIN_PASSWORD:
        login = input("Wrong password, try again: ")
        if login == "q":
            sys.exit(1)

    # Create a fernet and set a key for it
    global fernet 
    KEY = os.environ["KEY"].encode()
    fernet = Fernet(KEY)

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
        if choice == "gp": 
            username = input("Enter username: ")
            service = input("Enter service: ")
            add_password(service, username, generate_password())
            print("Done.\n")

        elif choice == "ap":
            username = input("Enter username: ")
            service = input("Enter service: ")
            password = input("Enter password: ")
            add_password(service, username, password)
            print("Done.\n")

        elif choice == "dl":
            username = input("Enter the username: ")
            delete_password(username)

        elif choice == "list":
            list_passwords()
            print()

        else:
            print("\n\nWrong choice, try again.\n")

        sleep(1)
        choice = userInterface()

def userInterface():
    print("\n"*3)
    print("*"*20)
    print("gp -> Generate Password")
    print("ap -> Add password")
    print("dl -> delete a password")
    print("list -> List all passwords")
    print("q to quit")
    print("*"*20)

    choice = input("Enter your choice: ").lower()

    return choice

def encrypt(password):
    encPassword = fernet.encrypt(password.encode()).decode()
    return encPassword

def decrypt(password):
    decPassword = fernet.decrypt(password.encode()).decode()
    return decPassword

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(chars) for i in range(12))
    return password

def add_password(service, username, password):
    password = encrypt(password)
    command = f'''INSERT INTO Passwords (Service, Username, Password)
    VALUES ('{service}', '{username}', '{password}')'''
    db.execute(command)
    db.commit()

def delete_password(username):
    command = f'''DELETE FROM Passwords WHERE Username="{username}"'''
    db.execute(command)
    db.commit()

def list_passwords():
    cursor = db.execute(f"SELECT * FROM Passwords")
    db.commit()

    for row in cursor.fetchall():
        print(f"Service: {row[0]:<10} Username: {row[1]:<10} Password: {decrypt(row[2]):<10}")

    input("\nPress Enter to continue..")

if __name__ == "__main__":
    main()