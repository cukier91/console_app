from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase

USER = 'postgres'
HOST = 'localhost'
PASSWORD = 'Ironmaiden6'


def create_db(db):
    try:
        connection = connect(user=USER, host=HOST, password=PASSWORD)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {db};")
    except DuplicateDatabase:
        return "Taka baza już istnieje "
    except OperationalError:
        return "Sprawdź dane logowania: Login i hasło "
    else:
        cursor.close()
        connection.close()

print(create_db('exam2'))