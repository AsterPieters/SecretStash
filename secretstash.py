#!/bin/python3
import os

from settings import *
from parse import parser
from sql import initialize_db
from encrypt import initialize_password

def check_password():
    password_path = PASSWORD_FILE_PATH
    if not os.path.exists(password_path):
        ##### Create password #####
        initialize_password()

##### Check if database exists #####
def check_stash():
    db_path = DATABASE_FILE_PATH
    if not os.path.exists(db_path):
        ##### Create database and initialize table #####
        initialize_db()

##### Main loop #####
if __name__ == "__main__":
    
    ##### Check if password & stash exists ####
    check_password()
    check_stash()

    ##### Take arguments #####
    parser()
