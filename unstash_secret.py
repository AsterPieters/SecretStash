from sql import execute_query

def unstash_secret(id, force_delete, password):

    if not force_delete:
        user_input = input('Are you sure? (y/N)')
        if user_input != 'y':
            return

    execute_query(f'DELETE FROM secrets WHERE id={id}')

