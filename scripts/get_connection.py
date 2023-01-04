import psycopg2
import psycopg2.extras


def db_connection():
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="Rabi@1991",
                                  cursor_factory=psycopg2.extras.RealDictCursor)
    return connection
