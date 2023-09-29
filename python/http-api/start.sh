#!/bin/bash

docker stop mongo-server
docker remove mongo-server
docker run --name mongo-server -d -p 27017-27019:27017-27019 mongo
docker container ls

python -m venv venv
source venv/Scripts/activate
pip install -q -r requirements.txt 
echo "Starting server.."
python src/server.py