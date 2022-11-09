# This function generate in password for the account from user
def generate_password():
    """ characters = "0AB12HIJKLM345node67893456,#@ab3456cde#@fghi3456jklmnodepqr,#@stuwxyzAB#@CDEFG.,#@HIJKLM.,#@NOPQAB0123RSTU#@WXYZ"
    length = 100
    sample = random.sample(characters, length)
    password_g = "".join(sample) """
    password_g = secrets.token_urlsafe(100)
    print(password_g)

    if passwordDecode  == password:
        print("The password is right")
        return True
    else:
        print("The password not is right")
        return False










import secrets
from cryptography.fernet import Fernet


# create users for go up to the data base
def create_user(family_name, password, given_name, picture, google_id, email, name):
    try:
        passwordCr, key = encryptPassword(password)
        check_password(passwordCr, password, key)
        user_inf = {
            "google_id": google_id,
            "name": name,
            "given_name": given_name,
            "family_name": family_name,
            "email": email,
            "password": passwordCr,
            "picture": picture,
        }
        
        print (" * Creating user" + user_inf['email'])
    except ValueError as error:
        print (" * Error creating")
        
    

# This function generate in password for the account from user
def generate_password():
    password_g = secrets.token_urlsafe(100)
    print (password_g)
    return password_g


# This function will encrypt the password and return the encrypted password
def encryptPassword(password):
    key = Fernet.generate_key()
    object_encryption = Fernet(key)
    encryptPassword = object_encryption.encrypt(str.encode(password))
    print ("\n")
    print (encryptPassword)
    return encryptPassword, object_encryption


# This function check if the password is correct
def check_password(passwordC, password, key):
    password_byte = key.decrypt(passwordC)
    passwordDecode = password_byte.decode()
    #print ("\n")
    #print(passwordDecode)
    if passwordDecode  == password:
        print("\n * The password is right")
        return True
    else:
        print("\n * The password not is right")
        return False