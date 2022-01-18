# Password Manager

## Database
Local database with a Master Password to access the database

## Password Generator
This program creates a random password for each instance that complies with present password requirements

## Setup
Clone repo
```
git clone https://github.com/AbdulmohsenA/PasswordManager
```

### Adjusting the .env file
You will fine a file called ADMIN.env has your Master password in order to access the database through this program.
```
DATABASE_PASSWORD = (Your password)
```

install requirements.txt
```
pip install requirements.txt
```

## Procedure
- Once you run PasswordManager.py is will make a database file named "PASSWORDS.db" and it will be using it.

## TODO
#### Functionality
- ~~**Finish Database**: Complete the main objective
- ~~**Delete passwords**: Add a functionality to delete the passwords
- **Clear database**: clear the whole database
- **Change master password**: Make a function to change the master password

#### Security
- **Secure the admin password**: Salt the login and hash it, and don't save the Admin password itself
- **Cypher the stored passwords**: Hash them in the database and decrypt them only when printing them
- **Only door is this program**: Make it so that the only way to see the passwords in the db is through this program (SEE ext)

#### Adjustments
- **Cleanup**: Optimize the code
