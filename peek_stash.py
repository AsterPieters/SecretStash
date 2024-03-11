from sql import execute_query
from encrypt import decrypt_string

def peek_stash(password):

    result = execute_query('SELECT id, website, account, salt FROM secrets', None, True)
    secrets = 0

    print('\n[ID] Website | Account')
    print('----------------------------------\n')
    for row in result:
        ##### Count the amount of secrets ######
        secrets += 1
        
        ##### Put the data in a dictionary #####
        encrypted_data = {
            'website': row[1],
            'account': row[2],
            'salt': row[3]
            }

        ##### Decrypt the data #####
        decrypted_data = decrypt_string(password, encrypted_data)

        print(f"[{row[0]}] {decrypted_data['website']} | {decrypted_data['account']}")


    print(f'\n{secrets} Secrets stashed\n')
