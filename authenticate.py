import hashlib
import secrets

from settings import *

def authenticate_user():

    ##### Ask for password #####
    user_input = input("Enter your password: ")

    ##### Get the salt #####
    with open(SALT_FILE_PATH, "r") as file:
        salt = file.readline()

    ##### Get the hashed master_password #####
    with open(PASSWORD_FILE_PATH, "r") as file:
        hashed_master_password = file.readline()

    ##### Salt and hash the user_input #####
    salted_user_input = user_input + salt
    hashed_user_input = hashlib.sha256(salted_user_input.encode()).hexdigest()

    ##### Compare user_input and master_password #####
    if hashed_user_input == hashed_master_password:
        return user_input
    
    else:
        return