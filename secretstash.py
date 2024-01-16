#!/bin/python3
import os

from parse import parser
from sql import initialize_db

##### Check if database exists #####
def check_stash():
    db_path = os.path.expanduser("~/.secretstash/stash.db")

    if not os.path.exists(db_path):
        print('[INFO] No stash found, creating new one.')

        ##### Create directory #####
        new_dir_name = ".secretstash"
        home_dir = os.path.expanduser("~")
        new_dir = os.path.join(home_dir, new_dir_name)
        os.makedirs(new_dir, exist_ok=True)

        ##### Create database and initialize table #####
        initialize_db()

##### Main loop #####
if __name__ == "__main__":
    
    ##### Check if stash exists ####
    check_stash()

    ##### Take arguments #####
    parser()