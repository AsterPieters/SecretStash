from sql import execute_query

def peek_stash():
    result = execute_query('SELECT id, website, account FROM secrets', None, True)
    secrets = 0

    print('\n[ID] Website | Account')
    print('----------------------------------\n')
    for row in result:
        secrets += 1
        print(f'[{row[0]}] {row[1]} | {row[2]}')
    print(f'\n{secrets} Secrets stashed\n')