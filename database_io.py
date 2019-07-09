import logging
from pathlib import Path
import sqlite3

PRIMARY_DATABASE = 'database.db'

def setup(LOG_FILE='logfile.log'):
    """Setup logging"""
    global logger

    # Setup logging
    logger = logging.getLogger(__name__)

    logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s')
    # Program started debug first log
    logger.debug('**database_io.py started**')


def create_database_table(tableSettings, DATABASE=PRIMARY_DATABASE):
    """Check if database exists, if not, create one"""
    logger.debug('Checking if database tables exists')
    if not Path(DATABASE).is_file():
        logger.warning('Database not found, creating new database')
        logger.debug(
            f'Database table settings: {tableSettings}, location "{DATABASE}"')
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute(tableSettings)
        conn.commit()
        conn.close()
        return False
    else:
        logger.debug('Database exists.')
        return True


def get_database_table(tableName, DATABASE=PRIMARY_DATABASE):
    """Return specified table from database"""
    logger.debug(f'Accessing database table {tableName}')
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(f"SELECT * FROM {tableName}")
    data = c.fetchall()
    conn.commit()
    conn.close()
    logger.debug(f'Database tables returned, data: {data}')
    return data


def delete_database_table(tableName, DATABASE=PRIMARY_DATABASE):
    """Remove specified table from database"""
    logger.info(f'Removing database table {tableName}')
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(f"DELETE * FROM {tableName}")
    conn.commit()
    conn.close()
    logger.debug(f'Database table {tableName} was deleted')


def remove_database_content(tableName, key, content, DATABASE=PRIMARY_DATABASE):
    """Remove specified content under key in table from database"""
    logger.info(
        f'Removing from database "{DATABASE}" with "{tableName}" as table name, under key "{key}" with content of "{content}"')
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("DELETE FROM :tableName WHERE :key=:content", {
              'tableName': tableName, 'id': key, 'content': content})
    conn.commit()
    conn.close()
    logger.debug('user unregistered')


def get_database_data(tableName, key, content, DATABASE=PRIMARY_DATABASE):
    """Return specified content nder key in table from database"""
    logger.debug(
        f'Retrieving from database "{DATABASE}" with "{tableName}" as table name, under key "{key}" with content of "{content}"')
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM :tableName WHERE :key=:content",
              {'tableName': tableName, 'key': key, 'content': content})
    fetch = c.fetchone()
    conn.commit()
    conn.close()
    return fetch


def add_to_database(tableName, values, DATABASE=PRIMARY_DATABASE):
    """Add new entry in specified table into database"""
    logger.debug(
        'Adding to database "{DATABASE}" to table "{tableName}" values: "{values}"')
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        if type(values) is str:
            c.execute("INSERT INTO :tableName VALUES(:values)", {
                      'tableName': tableName, 'values': values})
        elif type(values) is list or type(values) is tuple:
            str_values = ''
            for item in values:
                str_values += f' {item}'
            c.execute("INSERT INTO :tableName VALUES(:values)", {
                      'tableName': tableName, 'values': str_values[1:]})
        conn.commit()
        conn.close()
        logger.debug('Added successfully')
        return True
    except Exception as e:
        logger.error(
            f'unable to add: database "{DATABASE}" to table "{tableName}" values: "{values}"; Returned exception {e}.')
        return False


if __name__ == '__main__':
    setup()
