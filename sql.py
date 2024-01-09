import os
import sqlite3

def execute_query(query, values=None, fetch_result=None):
    ##### Connect or create db #####
    db_path = os.path.expanduser("~/.stash")
    conn = sqlite3.connect(db_path)

    ##### Create cursor #####
    cursor = conn.cursor()

    ##### Execute query #####
    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)
        
    ##### Print results #####
    result = cursor.fetchall()

    ##### Commit and close db #####
    conn.commit()
    conn.close()
    
    return result

def initialize_db():
    ##### Initialize db #####
    query = ('''
        CREATE TABLE IF NOT EXISTS secrets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            account TEXT NOT NULL,
            secret TEXT NOT NULL
            )
    ''')

    execute_query(query)

