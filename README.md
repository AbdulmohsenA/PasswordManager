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

install requirements.txt
```
pip install requirements.txt
```

## TODO
- **Finish Database**:
- **Secure the admin password**: Salt the login and hash it, and don't save the Admin password itself
- **Change master password**:
- **Cleanup**:
- **Cypher the stored passwords**: Hash them in the database and decrypt them only when printing them
- **Only door is this program**: Make it so that the only way to see the passwords in the db is through this program