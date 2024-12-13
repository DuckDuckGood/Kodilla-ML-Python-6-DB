import sqlite3
from sqlite3 import Error

def create_connection(db_name = ':memory:'):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        print(f'Successfully connected to {db_name} with Sqlite3 {sqlite3.sqlite_version}')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection(r'database.db')
    create_connection()