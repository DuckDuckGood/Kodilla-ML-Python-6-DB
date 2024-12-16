from colors import Colors
from queries_processing import insert_to_projects, insert_to_tasks, execute_script_sql, create_connection

def insert_data(conn):
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

if __name__ == '__main__':
    create_connection(insert_data, r'database.db')
    # create_connection()