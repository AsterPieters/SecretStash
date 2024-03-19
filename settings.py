import os

PASSWORD_FILE_PATH = os.path.expanduser("~/.secretstash/password.py")
SALT_FILE_PATH = os.path.expanduser("~/.secretstash/salt.py")
SECRET_STASH_PATH = os.path.expanduser("~/.secretstash/")
DATABASE_FILE_PATH = os.path.expanduser("~/.secretstash/stash.db")

AUTO_CREATED_PASSWORD_LENGTH = 12