from sql import execute_query
from encrypt import decrypt_string

def reveal_secret(id, password):

    ##### Print chosen Secret #####
    result = execute_query(f'SELECT secret, salt FROM secrets WHERE id={id}', None, True)
    for row in result:

        encrypted_data = {
                'password': row[0],
                'salt': row[1]
                }

        decrypted_secret = decrypt_string(password, encrypted_data)
        print(f"{decrypted_secret['password']}")
