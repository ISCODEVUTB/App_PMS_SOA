from os import abort
import random
import secrets
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash


# create users for go up to the data base
def create_user(family_name, password, given_name, picture, google_id, email, name):
    try:
        passwordCr = encryptPassword(password)
        check_password(passwordCr, password)
        user_inf = {
            "google_id": google_id,
            "name": name,
            "given_name": given_name,
            "family_name": family_name,
            "email": email,
            "password": passwordCr,
            "picture": picture,
        }
        
        print ("Creating user: " + user_inf["email"])
        
        return jsonify({"data": user_inf})
    except Exception as error:
        print ("Error creating")
        
    
# This function generate in password for the account from user
def generate_password():
    password_g = secrets.token_urlsafe(100)
    print (password_g)
    return password_g


# This function will encrypt the password and return the encrypted password
def encryptPassword(password):
    passwordC = generate_password_hash(password)
    return passwordC


# This function check if the password is correct
def check_password(passwordC, password):
    if check_password_hash(passwordC, password) == True:
        print("The password is right")
        return True
    else:
        print("The password not is right")
        return False