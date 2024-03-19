from sql import execute_query
from peek_stash import show_entry_by_id

def unstash_secret(id, force_delete, password):

    if not force_delete:
        show_entry_by_id(password, id)
        user_input = input('This entry will be permanently deleted,\nAre you sure? (y/N) ')
        if user_input != 'y':
            return

    execute_query(f'DELETE FROM secrets WHERE id={id}')

