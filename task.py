from queries_processing import create_connection
from colors import Colors

class Task:
    def __init__(self, retrieved_data):
        self.id = retrieved_data[0]
        self.project_id = retrieved_data[1]
        self.name = retrieved_data[2]
        self.description = retrieved_data[3]
        self.status = retrieved_data[4]
        self.start_date = retrieved_data[5]
        self.end_date = retrieved_data[6]

    def __retrieve_project_name(self):
        def get_it(conn):
            cursor = conn.cursor()
            cursor.execute(f'select name from projects where id = {self.project_id}')
            return cursor.fetchone()[0]


        return create_connection(get_it, r'database.db')

    def __str__(self):
        return f'{Colors.OKBLUE}ID: {self.id}{Colors.ENDC} | Task: {self.name} | Project: {self.__retrieve_project_name()} | Description: {self.description} | Status: {self.status} | Start Date: {self.start_date} | End Date: {self.end_date}'