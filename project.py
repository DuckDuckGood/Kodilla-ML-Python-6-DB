from colors import Colors

class Project:
    def __init__(self, fetched_data):
        self.id = fetched_data[0]
        self.name = fetched_data[1]
        self.date_from = fetched_data[2]
        self.date_to = fetched_data[3]

    def __str__(self):
        return f'{Colors.OKBLUE}ID: {self.id}{Colors.ENDC} | Project: {self.name} | Starting: {self.date_from} | Ending: {self.date_to}'