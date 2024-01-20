from sql import execute_query
from encrypt import decrypt_string
from authenticate import authenticate_user

def peek_stash():
    if (password := authenticate_user()):
        result = execute_query('SELECT id, website, account FROM secrets', None, True)
        secrets = 0

        print('\n[ID] Website | Account')
        print('----------------------------------\n')
        for row in result:
            secrets += 1
            decrypted_website = decrypt_string(password, row[1])
            decrypted_account = decrypt_string(password, row[2])

            print(f'[{row[0]}] {decrypted_website} | {decrypted_account}')


        print(f'\n{secrets} Secrets stashed\n')