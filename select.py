from queries_processing import create_connection
from colors import Colors
from project import Project
from task import Task

def select_projects(conn):
    print(f"{Colors.HEADER}Retrieving data from 'projects'...{Colors.ENDC}\n")
    cursor = conn.cursor()
    retrieved = cursor.execute('SELECT * FROM projects')
    result = []
    for row in retrieved:
        mapped = Project(row)
        print(mapped)
        result.append(mapped)
    return result

def select_tasks(conn):
    print(f"{Colors.HEADER}Retrieving data from 'tasks'...{Colors.ENDC}\n")
    cursor = conn.cursor()
    retrieved = cursor.execute('SELECT * FROM tasks')
    result = []
    for row in retrieved:
        mapped = Task(row)
        print(mapped)
        result.append(mapped)
    return result

if __name__ == '__main__':
    create_connection(select_projects, r'database.db')