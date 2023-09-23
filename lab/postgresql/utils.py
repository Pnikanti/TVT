# Maintainer: Patrick Nikanti 2023

import json

def parse_json(filepath: str, ignore_file_not_found: bool = True):
    """
    Reads and returns a JSON file.
    """
    try:
        # Read credentials from file
        with open(filepath, "r") as handle:
            return json.load(handle)
    except FileNotFoundError as err:
        if not ignore_file_not_found:
            raise err
        return None
            
    