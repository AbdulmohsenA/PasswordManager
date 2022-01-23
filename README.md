# Password Manager


## Features

### Database
Local database with a Master Password to access the database.

### Ciphered Passwords
Passwords loaded into the database will be encrypted. And will be decrypted only for viewing through this program.

### Password Generator
Create a random password for each username that complies with present password requirements, you don't need to reuse your own passwords.

---

## Setup
Clone repo
```
git clone https://github.com/AbdulmohsenA/PasswordManager
```
install requirements.txt
```
pip install requirements.txt
```

### Procedure
Run `setup.py` to initialize your secret info (Master password, KEY, etc..). `setup.py` will delete itself after the first run, so choose your password wisely.  
After that. Run `PasswordManager.py` to initialize your database and to start using the program.

---
 
## TODO
#### Functionality
- ~~**Finish Database**: Complete the main objective~~
- ~~**Delete passwords**: Add a functionality to delete the passwords~~
- **Clear database**: clear the whole database
- **Change master password**: Make a function to change the master password

#### Security
- **Secure the admin password**: Salt the login and hash it, and don't save the Admin password itself
- ~~**Cipher the stored passwords**: Encrypt them in the database and decrypt them only when printing them~~
- **Only door is this program**: Make it so that the only way to see the passwords in the db is through this program (SEE ext)

#### Adjustments
- **Cleanup**: Optimize the code
