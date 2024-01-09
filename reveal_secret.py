from sql import execute_query

def reveal_secret(id):

    ##### Print chosen Secret #####
    result = execute_query(f'SELECT secret FROM secrets WHERE id={id}', None, True)
    for row in result:
        print(f'{row[0]}')
