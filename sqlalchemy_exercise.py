import csv
from sqlalchemy import create_engine, Table, Column, String, MetaData, Integer

def retrieve_csv_by_name(file_name):
    with open(f'sqlalchemy_exercise/{file_name}', 'r') as csv_file:
        reader = csv.reader(csv_file)
        return list(reader)

meta = MetaData()
measures = Table('clean_measures', meta,
                 Column('id', Integer, primary_key=True),
                 Column('station', String),
                 Column('date', String),
                 Column('precip', String),
                 Column('tobs', Integer)
)

stations = Table('clean_stations', meta, Column('id', Integer, primary_key=True),
                 Column('station', String),
                 Column('latitude', String),
                 Column('longitude', String),
                 Column('elevation', String),
                 Column('name', String),
                 Column('country', String),
                 Column('state', String),
)

engine = create_engine('sqlite:///sqlalchemy_exercise/exercise_database.db')

meta.create_all(engine)
connection = engine.connect()

for measure in retrieve_csv_by_name('clean_measure.csv'):
    try:
        measure_insert = measures.insert().values(station=measure[0], date=measure[1], precip=measure[2], tobs=measure[3])
        connection.execute(measure_insert)
    except Exception as e:
        print('measure_error', e)

for station in retrieve_csv_by_name('clean_stations.csv'):
    try:
        station_insert = stations.insert().values(station=station[0], latitude=station[1], longitude=station[2], elevation=station[3], name=station[4], country=station[5], state=station[6])
        connection.execute(station_insert)
    except Exception as e:
        print('station_error', e)
