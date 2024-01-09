import os
import sqlite3

def execute_query(query, values=None):
    ##### Connect or create db #####
    db_path = os.path.expanduser("~/.stash")
    conn = sqlite3.connect(db_path)
    print("[INFO] Connected to database successfully.")

    ##### Create cursor #####
    cursor = conn.cursor()

    ##### Execute query #####
    cursor.execute(query, values)

    ##### Commit and close db #####
    conn.commit()
    conn.close()

    print("[INFO] Query executed successfully.")

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

