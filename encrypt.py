from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
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
        salt=salt.encode('utf-8'),
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode('utf-8'))
    
    ##### Serialize the key so it gets accepts by fernet #####
    key = base64.urlsafe_b64encode(key)
    
    return key

def encrypt_string(password, string):

    ##### Generate salt #####
    salt = "TODO"

    ##### Salt and generate the key  #####
    key = generate_key_from_password(password, salt)
    cipher_suite = Fernet(key)

    print(cipher_suite)
    ##### Encrypt the string #####
    encrypted_string = cipher_suite.encrypt(string.encode('utf-8'))

    return encrypted_string

def decrypt_string(password, encrypted_string):

    if isinstance(encrypted_string, int):
        # If encrypted_string is an integer, convert it to bytes
        encrypted_string = encrypted_string.to_bytes((encrypted_string.bit_length() + 7) // 8, 'big')

    ##### Generate salt #####
    salt = "TODO"

    ##### Salt and generate the key  #####
    key = generate_key_from_password(password, salt)
    cipher_suite = Fernet(key)
    
    decrypted_string = cipher_suite.decrypt(encrypted_string).decode('utf-8')


    return decrypted_string