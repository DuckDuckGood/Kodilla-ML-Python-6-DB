from queries_processing import create_connection

def delete_from_projects_by_id(conn):
    project_id = input('Please provide the project ID, which you want to delete: ')
    conn.cursor().execute('DELETE FROM projects WHERE id = ?', (project_id,))
    conn.commit()

create_connection(delete_from_projects_by_id, r'database.db')