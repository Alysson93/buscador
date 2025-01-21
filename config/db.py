from sqlite3 import Connection, Row
from config.settings import Settings

def get_db_conn():
    try:
        connection = Connection(Settings().DATABASE_URL, check_same_thread=False)
        connection.row_factory = Row
        yield connection
    finally:
        connection.close()
