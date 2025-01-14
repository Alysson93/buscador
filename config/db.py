from sqlite3 import Connection, Row


def get_db_conn():
    try:
        connection = Connection('database.db', check_same_thread=False)
        connection.row_factory = Row
        yield connection
    finally:
        connection.close()
