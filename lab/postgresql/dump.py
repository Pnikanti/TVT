# Maintainer: Patrick Nikanti 2023

import sys
import time
import json
from utils import parse_json
from psycopg2._psycopg import cursor as psqlcursor
from connect import Connect, connect

def dump(dbname: str, table: str, filepath: str, credentials_filepath: str = "secrets.json"):
    """
    Dump JSON in to a psql database.
    """
    secrets: dict = parse_json(filepath=credentials_filepath)
    
    with open(filepath, "r") as handle:
        data: str = json.load(handle)

    psql: Connect = connect(
        dbname=dbname,
        user=secrets['user'],
        password=secrets['password'],
        host=secrets['host'],
        port=secrets['port']
    )
    database: psqlcursor = psql.database
    database.execute(
        f"SELECT count(*) from {table}"
    )

    id = database.fetchone()[0]
    now = int(time.time())
    database.execute(
        f"INSERT INTO {table} (id, timestamp, data) VALUES({id}, {now}, '{json.dumps(data)}')"
    )

if __name__ == '__main__':
    dbname = str(sys.argv[1])
    table = str(sys.argv[2])
    filepath = str(sys.argv[3])
    
    dump(
        dbname=dbname,
        table=table,
        filepath=filepath
    )
