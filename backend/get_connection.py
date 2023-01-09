import psycopg2
import psycopg2.extras


def db_connection():
    connection = psycopg2.connect(dbname="postgres",
                                  user="postgres",
                                  password="Rabi@1991",
                                  # host="host.docker.internal",
                                host="localhost",
                                  port='5432',
                                  cursor_factory=psycopg2.extras.RealDictCursor)
    return connection
