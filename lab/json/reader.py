import json
import sys

def main():
    try:
        filename = sys.argv[1]
    except Exception as e:
        raise Exception("Usage: reader.py path/to/a/file.json") from e
    
    with open(filename, 'r') as handle:
        print(json.load(handle))

if __name__ == '__main__':
    main()