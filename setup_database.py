import argparse

from sqlalchemy import create_engine

# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", default="postgres")
parser.add_argument("-hst", "--host", default="localhost")
parser.add_argument("-p", "--port", default="5432")
parser.add_argument("-d", "--database", default="product")

args = vars(parser.parse_args())
username = args["username"]
host = args["host"]
port = args["port"]
database = args["database"]

# create the database from the main database (postgresql)
connection_string = f"postgresql://{username}@{host}:{port}/postgres"
engine = create_engine(connection_string)
connection = engine.connect()
connection.execute("COMMIT")
connection.execute(f"CREATE DATABASE {database}")
connection.close()

# setup the new database
connection_string = f"postgresql://{username}@{host}:{port}/{database}"
engine = create_engine(connection_string)
with engine.connect() as connection:
    connection.execute("CREATE SCHEMA app")
    connection.execute("""
                       CREATE TABLE app.product(
                        id serial PRIMARY KEY,
                        name VARCHAR (500),
                        rating INTEGER,
                        vol INTEGER,
                        year INTEGER)
                       """)
