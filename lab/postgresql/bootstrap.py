# Maintainer: Patrick Nikanti 2023

import sys
from psycopg2._psycopg import cursor as psqlcursor
from connect import Connect, connect

psql: Connect = connect()
database : psqlcursor = psql.database

def bootstrap(database_name: str):
    """
    ** Convenience function to setup a psql database to a lab environment. **

    Bootstrap a database with predefined 'posts' table.

    Table 'posts'

    - post_id (SERIAL PK)
    - post_timestamp (TIMESTAMP NOT NULL)
    - post_data (JSON NOT NULL)
    """
    global psql
    global database

    database.execute(
        f"""SELECT (datname) FROM pg_database WHERE datname = '{database_name}'"""
    )
    db_exists = database.fetchone()

    if (db_exists):
        print(f"Database '{database_name}' already exists")
        return

    database.execute(
        f"""CREATE DATABASE {database_name}"""
    )

    # CREATE A NEW CONNECTION
    psql.session.close()
    psql = connect(dbname=database_name)
    database = psql.database
    
    database.execute(
        f"""CREATE TABLE posts (
            id SERIAL PRIMARY KEY,
            timestamp INTEGER NOT NULL,
            data JSON
        )"""
    )

if __name__ == '__main__':
    if sys.argv[1] != "iknowwhatiamdoing":
        print("You don't know what you're doing. Exiting..")
        exit(0)

    if database_name := str(sys.argv[2]):
        bootstrap(
            database_name=database_name
        )
