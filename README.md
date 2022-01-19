# Password Manager


## Features

### Database
Local database with a Master Password to access the database.

### Ciphered Passwords
Passwords loaded into the database will be encrypted. And will be decrypted through this program.

### Password Generator
Create a random password for each username that complies with present password requirements, you don't need to reuse your own passwords.

## Setup
Clone repo
```
git clone https://github.com/AbdulmohsenA/PasswordManager
```

### Adjusting the .env file
You will find a file called ADMIN.env which will contain your secret information.

`DATABASE_PASSWORD` is the Master password in order to access the database through this program.  
`KEY` is a key to encrypt and decrypt your passwords.  
```
DATABASE_PASSWORD = (Your password)
KEY = (KEY)
```

install requirements.txt
```
pip install requirements.txt
```

## Procedure
- Once you run PasswordManager.py is will make a database file named "PASSWORDS.db" and it will be using it.

## TODO
#### Functionality
- ~~**Finish Database**: Complete the main objective~~
- ~~**Delete passwords**: Add a functionality to delete the passwords~~
- **Clear database**: clear the whole database
- **Change master password**: Make a function to change the master password

#### Security
- **Secure the admin password**: Salt the login and hash it, and don't save the Admin password itself
- ~~**Cypher the stored passwords**: Encrypt them in the database and decrypt them only when printing them~~
- **Only door is this program**: Make it so that the only way to see the passwords in the db is through this program (SEE ext)

#### Adjustments
- **Cleanup**: Optimize the code
