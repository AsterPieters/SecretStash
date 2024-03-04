import hashlib
import secrets

from settings import *

def authenticate_user(password):

    if password:
        ##### Get the salt #####
        with open(SALT_FILE_PATH, "r") as file:
            salt = file.readline()

        ##### Get the hashed master_password #####
        with open(PASSWORD_FILE_PATH, "r") as file:
            hashed_master_password = file.readline()

        ##### Salt and hash the user_input #####
        salted_password = str(password) + str(salt)
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        ##### Compare user_input and master_password #####
        if hashed_password == hashed_master_password:
            return password
        
        else:
            print("Password incorrect.")
            return False

    else:
        print("Usage: secretstash PASSWORD COMMAND")

def ask_password(): ##### Ask password if user did not provide #####

    password = input("Password: ")
    return password

