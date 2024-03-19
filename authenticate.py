import hashlib
import secrets
import logging

from settings import *
import getpass as gp

def ask_password():
    """ Ask user for the password if not given by flag"""
    
    attempts = 0

    while attempts < 3:

        # Ask securely for password
        user_password_given = gp.getpass(prompt='Password: ', stream=None)
        result = check_password(user_password_given)
        if result == False:
            attempts += 1
        else:
            break

    return result

def check_password(password):
    """ Hash and compare the input to the password

    Args:
        password: The users master password
    """

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
        print("Password incorrect.\n") 
        return False
