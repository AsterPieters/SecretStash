from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import secrets
import hashlib
import base64
import os

from settings import *

def hash_string(string):
    ##### Generate salt #####
    salt = secrets.token_hex(16)

    ##### Salt and hash the string #####
    salted_string = string + salt
    hashed_string = hashlib.sha256(salted_string.encode()).hexdigest()
    
    return hashed_string, salt

def initialize_password():
    ##### Ask master password from user #####
    string = input("Enter your master password\nAll secrets will be irrecoverable when this password is lost!\n# ")
    hashed_string, salt = hash_string(string)

    ##### Create the password file #####
    with open(PASSWORD_FILE_PATH, "w") as file:
        file.write(hashed_string)

    ##### Create the salt file #####
    with open(SALT_FILE_PATH, "w") as file:
        file.write(salt)
        
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
    return hashed_user_input == hashed_master_password
