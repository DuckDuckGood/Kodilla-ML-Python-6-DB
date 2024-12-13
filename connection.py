import sqlite3
from sqlite3 import Error
from colors import Colors
from queries_processing import insert_to_projects, insert_to_tasks, execute_script_sql

def what_to_do(conn):
    options = (
        "insert to 'projects'",
        "insert to 'tasks'",
        "execute 'script.sql'",
    )

    print(f'{Colors.UNDERLINE}What do you want to do?{Colors.ENDC}')
    for option in enumerate(options):
        print(f'{Colors.HEADER}{option[0]+1}. {Colors.ENDC}{option[1]}')
    choosen_option = input('Type number from 1 to 3: ')
    if choosen_option.isnumeric():
        option_number = int(choosen_option)
        if option_number > 0 and not option_number > len(options):
            match option_number:
                case 1:
                    insert_to_projects(conn)
                case 2:
                    insert_to_tasks(conn)
                case 3:
                    execute_script_sql(conn)
            return
    print(f'{Colors.FAIL}There is not option like "{choosen_option}"{Colors.ENDC}')

def create_connection(db_name = ':memory:'):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        print(f'{Colors.OKGREEN}Successfully connected to {db_name} with Sqlite3 {sqlite3.sqlite_version}{Colors.ENDC}\n')

        what_to_do(conn)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection(r'database.db')
    # create_connection()