from sql import execute_query
from authenticate import authenticate_user
from encrypt import encrypt_string

def stash_secret(website, account, secret):

    if (password := authenticate_user()):

        ##### Encrypt the data #####
        encrypted_website = encrypt_string(password, website)
        encrypted_account = encrypt_string(password, account)
        encrypted_secret = encrypt_string(password, secret)

        ##### This looks unnecessary but it prevents SQL injection #####
        insert_query = "INSERT INTO secrets (website, account, secret) VALUES (?, ?, ?)"
        execute_query(insert_query, (encrypted_website, encrypted_account, encrypted_secret))

    else:
        return