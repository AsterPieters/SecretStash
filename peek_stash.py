from sql import execute_query

def peek_stash():
    result = execute_query('SELECT * FROM secrets', None, True)

    print('ID | Website | Account')
    print('----------------------------------\n')
    for row in result:

        print(f'{row[0]} | {row[1]} | {row[2]}')
