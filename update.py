from sqlite3 import Error
from queries_processing import create_connection, update_project_name, update_task_name
from select import select_tasks, select_projects

def find_by_id(data_list, by_id):
    if len(data_list) != 0:
        for element in data_list:
            if int(element.id) == int(by_id):
                return element
    return None

def update_project_or_task(conn):
    what_to_update = input("What to update? (1 for project, 2 for task): ")
    retrieved = []
    if what_to_update == "1":
        retrieved = select_projects(conn)
    elif what_to_update == "2":
        retrieved = select_tasks(conn)
    if len(retrieved) == 0:
        print('There is no data')
        return
    to_update_id = input("Which one do you want to update the name? (Type it's ID): ")
    found = find_by_id(retrieved, to_update_id)
    found.name = input(f'Please type new name ({found.name}): ')

    if what_to_update == "1":
        update_project_name(conn, found)
    elif what_to_update == "2":
        update_task_name(conn, found)

def update_project_by_query(conn, **kwargs):
    project_id = kwargs.get("id")
    if project_id is not None:
        keys = ', '.join([f'{k} = ?' for k in kwargs.keys()])
        values = tuple(value for value in kwargs.values())
        try:
            conn.cursor().execute(f'update projects set {keys} where id = {project_id}', values)
            conn.commit()
        except Error as e:
            print(e)

if __name__ == '__main__':
    create_connection(update_project_by_query, r'database.db', id=1, name='Updated by function "update_project_by_query"!')