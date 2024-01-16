import os
import sqlite3

from settings import *

def execute_query(query, values=None, fetch_result=None):
    ##### Connect to DB #####
    db_path = DATABASE_FILE_PATH
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

    print('[INFO] No stash found, creating new one.')

    ##### Create directory #####
    new_dir = SECRET_STASH_PATH
    os.makedirs(new_dir, exist_ok=True)

    ##### Create & initialize db #####
    query = ('''
        CREATE TABLE IF NOT EXISTS secrets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            account TEXT NOT NULL,
            secret TEXT NOT NULL
            )
    ''')

    execute_query(query)

