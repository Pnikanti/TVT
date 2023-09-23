#!/bin/bash

IMAGE=lab_environment
CONTAINER=lab_container

if [[ -z $1 ]]; then
    echo "Pass either 'start' or 'build' as first argument."
    exit 0
fi

if [[ $1 == "start" ]]; then
    echo "Starting.."
    docker start $CONTAINER
    docker exec -it $CONTAINER bash
fi

if [[ $1 == "build" ]]; then
    echo "Building.."
    docker build -t $IMAGE .
    docker run -dit -p 5432:5432 --name $CONTAINER $IMAGE
fi

if [[ $1 == "prune" ]]; then
    echo "Pruning.."
    docker stop $CONTAINER
    docker rm $CONTAINER
fi