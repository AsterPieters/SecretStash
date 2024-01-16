from sql import execute_query

def stash_secret(website, account, secret, password):

    ##### This looks unnecessary but it prevents SQL injection #####
    insert_query = "INSERT INTO secrets (website, account, secret) VALUES (?, ?, ?)"
    execute_query(insert_query, (website, account, secret))
