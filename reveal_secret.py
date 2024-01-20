from sql import execute_query
from encrypt import decrypt_string
from authenticate import authenticate_user

def reveal_secret(id):
    if (password := authenticate_user()):

        ##### Print chosen Secret #####
        result = execute_query(f'SELECT secret FROM secrets WH  ERE id={id}', None, True)
        for row in result:
            decrypted_secret = decrypt_string(password, row[0])
            print(f'{decrypted_secret}')
    else:
        return