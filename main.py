# TODO create a GUI (Tkinter) that will have a master password and after unlocking, it will store all of yours E-Mail addresses & passwords
import logging
from pathlib import Path
import hashlib
import sqlite3
import database_io as dtbase

# Path to user database
DATABASE = 'datbase.db'
# Path to logging file
LOG_FILE = 'logfile.log'


# Setup logging
logger = logging.getLogger(__name__)

logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s')

# Setup logging in database_io.py
dtbase.setup(LOG_FILE)

# Create main database with emails
dtbase.create_database_table("""CREATE TABLE emails (
                name TEXT,
                email TEXT,
                password TEXT
            )""")
