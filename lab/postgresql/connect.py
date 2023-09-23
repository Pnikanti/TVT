# Maintainer: Patrick Nikanti 2023

import psycopg2
from utils import parse_json
from psycopg2._psycopg import connection as psqlconnection
from psycopg2._psycopg import cursor as psqlcursor

class Connect:
    """
    Container for a psql connection.
    """
    def __init__(
            self,
            session: psqlconnection,
            database: psqlcursor
        ):
        self.session: psycopg2.connection = session
        self.database: psycopg2.cursor = database

def connect(filepath: str = "secrets.json", **kwargs) -> Connect:
    """
    Connect to a psql database with a configuration file.
    Use keyword arguments (kwargs) to override configuration variables.

    Returns dict
    {
        "session": psycopg2.connect,
        "database": psycopg2.cursor
    }
    """
    secrets: dict = parse_json(filepath=filepath if filepath else "secrets.json")

    return _connect(
        dbname=kwargs.get('dbname', secrets['dbname']),
        user=kwargs.get('user', secrets['user']),
        password=kwargs.get('password', secrets['password']),
        host=kwargs.get('host', secrets['host']),
        port=kwargs.get('port', secrets['port'])
    )

def _connect(
    dbname: str,
    user: str,
    password: str,
    host: str,
    port: int
) -> Connect:
    """
    Connect to a psql database.
    
    Returns dict
    {
        "session": psycopg2.connect,
        "database": psycopg2.cursor
    }
    """
    # Open a connection with psql database
    session: psqlconnection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    # Autocommit queries
    session.autocommit = True
    # Create a cursor object to interact with the database
    database: psqlcursor = session.cursor()

    return Connect(
        session=session,
        database=database
    )
    