#!/bin/python3
import os

from parse import parser
from sql import initialize_db

##### Check if database exists #####
def check_stash():
    db_path = os.path.expanduser("~/.stash")
    if not os.path.exists(db_path):

        ##### Create database and initialize table #####
        print('[INFO] No stash found, creating new one.')
        initialize_db()

##### Main loop #####
if __name__ == "__main__":
    
    ##### Check if stash exists ####
    check_stash()

    ##### Take arguments #####
    parser()