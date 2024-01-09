import os
import sqlite3

def execute_query(query):
    ##### Connect or create db #####
    db_path = os.path.expanduser("~/.stash")
    conn = sqlite3.connect(db_path)
    print("[INFO] Connected to database succesfully.")

    ##### Create cursor #####
    cursor = conn.cursor()

    ##### Execute query #####
    cursor.execute(query)

    ##### Commit and close db #####
    conn.commit()
    conn.close()

    print("[INFO] Query executed succesfully.")

def initialize_db():
    ##### Initialize db #####
    query = ('''
        CREATE TABLE IF NOT EXISTS secrets (
            id INTEGER PRIMARY KEY,
            website TEXT NOT NULL,
            account TEXT NOT NULL,
            secret TEXT NOT NULL,
            note TEXT
            )
    ''')

    execute_query(query)

