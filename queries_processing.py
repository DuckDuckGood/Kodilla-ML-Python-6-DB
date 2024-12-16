import sqlite3
from sqlite3 import Error
from colors import Colors

def create_connection(what_to_do, db_name = ':memory:', **kwargs):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        print(f'{Colors.OKGREEN}Successfully connected to {db_name} with Sqlite3 {sqlite3.sqlite_version}{Colors.ENDC}\n')
        result = what_to_do(conn, **kwargs)
        conn.close()
        return result
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def insert_to_projects(conn):
    name = input('Name: ')
    start_date = input('Start date: ')
    end_date = input('End date: ')

    lastrowid = conn.cursor().execute('insert into projects (name, start_date, end_date) values (?, ?, ?)', (name, start_date, end_date)).lastrowid
    conn.commit()
    print(f"Your data has been added to table 'projects' with id={lastrowid}")

def insert_to_tasks(conn):
    project_id = input('Project ID: ')
    name = input('Name: ')
    description = input('Description: ')
    status = input('Status: ')
    start_date = input('Start date: ')
    end_date = input('End date: ')

    lastrowid = conn.cursor().execute('insert into tasks (project_id, name, description, status, start_date, end_date) values (?, ?, ?, ?, ?, ?)', (project_id, name, description, status, start_date, end_date)).lastrowid
    conn.commit()
    print(f"Your data has been added to table 'tasks' with id={lastrowid}")

def execute_script_sql(conn):
    with open('script.sql', 'r') as script:
        for enumerated_query in enumerate(script):
            execute_query(conn, enumerated_query)
    conn.commit()

def execute_query(conn, enumerated_query):
    query_index = enumerated_query[0]
    query = enumerated_query[1]

    print('Executing query:')
    print(f'{query_index}. {Colors.HEADER}{query}{Colors.ENDC}\n')
    cursor = conn.cursor()
    cursor.execute(query)

def update_project_name(conn, project):
    conn.cursor().execute('update projects set name=? where id=?', (project.name, project.id))
    conn.commit()

def update_task_name(conn, task):
    conn.cursor().execute('update tasks set name=? where id=?', (task.name, task.id))
    conn.commit()
