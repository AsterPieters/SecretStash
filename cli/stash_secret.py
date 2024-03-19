from sql import execute_query
from encrypt import encrypt_string, create_password

def stash_secret(website, account, secret, password):

    if not secret:
        secret = create_password()

    ##### Encrypt the data #####
    encrypted_data = encrypt_string(password, {
        'website': website,
        'account': account,
        'secret': secret})

    ##### This looks unnecessary but it prevents SQL injection #####
    insert_query = "INSERT INTO secrets (website, account, secret, salt) VALUES (?, ?, ?, ?)"
    execute_query(insert_query, (encrypted_data['website'], encrypted_data['account'], encrypted_data['secret'], encrypted_data['salt']))
