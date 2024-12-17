from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine('sqlite:///database.db')

meta = MetaData()
students = Table('students', meta, Column('id', Integer, primary_key=True), Column('name', String), Column('last_name', String))
meta.create_all(engine)
print(engine.table_names())

students_insert = students.insert().values(name='John', last_name='Doe')
print(students_insert.compile().params)

students_select = students.select()

connection = engine.connect()
connection.execute(students_insert)
for row in connection.execute(students_select):
    print(row)
