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

    - id (SERIAL PK)
    - username (VARCHAR(20) NOT NULL)
    - timestamp (INTEGER NOT NULL)
    - data (JSON NOT NULL)
    """
    global psql
    global database

    database.execute(
        f"""SELECT (usename) FROM pg_catalog.pg_user WHERE usename = 'admin'"""
    )
    user_exists = database.fetchone()

    # TODO: Change hardcoded credentials to be fetched from a secrets file
    # TODO: Add this task to a branch and make it a separate Moodle task.
    
    if (user_exists):
        print(f"User 'admin' exists, not creating a new one")
    else:
        database.execute(
            f"""CREATE USER 'admin' WITH SUPERUSER PASSWORD 'admin'"""
        )

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
            username VARCHAR (20) NOT NULL,
            timestamp INTEGER NOT NULL,
            data JSON
        )"""
    )

if __name__ == '__main__':
    if sys.argv[1] != "iknowwhatiamdoing":
        print("You don't know what you're doing. Exiting..")
        exit(0)

    if database_name := str(sys.argv[2]).lower():
        bootstrap(
            database_name=database_name
        )
