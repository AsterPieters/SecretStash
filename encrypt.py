from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.fernet import Fernet
import secrets
import hashlib
import bcrypt
import base64
import os
import secrets
import string

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

    ##### Create secretstash directory #####
    new_dir = SECRET_STASH_PATH
    os.makedirs(new_dir, exist_ok=True)

    ##### Create the password file #####
    with open(PASSWORD_FILE_PATH, "w") as file:
        file.write(hashed_string)

    ##### Create the salt file #####
    with open(SALT_FILE_PATH, "w") as file:
        file.write(salt)

def generate_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode('utf-8'))
    
    ##### Serialize the key so it gets accepts by fernet #####
    key = base64.urlsafe_b64encode(key)
    
    return key

def encrypt_string(password, data):

    ##### Generate salt #####
    salt = bcrypt.gensalt()

    ##### Initiate dictionary #####
    encrypted_data = {}

    ##### Generate the key #####
    key = generate_key_from_password(password, salt)
    cipher_suite = Fernet(key)

    ##### Loop over the data #####
    for field, data in data.items():

        ##### Encrypt the string #####
        encrypted_data[field] = cipher_suite.encrypt(data.encode('utf-8'))

    ##### Add salt to the data #####
    encrypted_data['salt'] = salt

    return encrypted_data

def decrypt_string(password, encrypted_data):

    ##### Initiate dictionary #####
    decrypted_data = {}

    ##### Salt and generate the key  #####
    key = generate_key_from_password(password, encrypted_data['salt'])
    cipher_suite = Fernet(key)

    ##### Remove the salt from the data #####
    del encrypted_data['salt']

    ##### Loop over the data #####
    for field, data in encrypted_data.items():
        decrypted_data[field] = cipher_suite.decrypt(data).decode('utf-8')

    return decrypted_data

def create_password():
    length = AUTO_CREATED_PASSWORD_LENGTH
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password