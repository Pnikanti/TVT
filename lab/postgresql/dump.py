# Maintainer: Patrick Nikanti 2023

import sys
import os
import time
import json
from psycopg2._psycopg import cursor as psqlcursor
from connect import Connect, connect

def dump(db_name: str, table: str, filepath: str, credentials_filepath: str = "secrets.json"):
    """
    Dump JSON file into a psql table.
    """
    psql: Connect = connect(dbname=db_name)
    database: psqlcursor = psql.database
    database.execute(
        f"SELECT count(*) from {table}"
    )

    with open(filepath, "r") as handle:
        data: str = json.load(handle)
    id = database.fetchone()[0]
    now = int(time.time())
    username = os.getlogin()

    database.execute(
        f"INSERT INTO {table} (id, username, timestamp, data) VALUES({id}, {username}, {now}, '{json.dumps(data)}')"
    )

if __name__ == '__main__':
    db_name = str(sys.argv[1])
    table = str(sys.argv[2])
    filepath = str(sys.argv[3])
    
    dump(
        dbname=db_name,
        table=table,
        filepath=filepath
    )
