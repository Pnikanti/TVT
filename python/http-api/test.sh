#!/bin/bash

curl -X POST -H "Content-type: application/json" -d "{\"username\" : \"John Doe\", \"body\" : \"Mietintöjä..\"}" "localhost:5000/mietteet"