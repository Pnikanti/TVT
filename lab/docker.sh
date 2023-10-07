#!/bin/bash

IMAGE=lab_environment
CONTAINER=lab_container

function start() {
    echo "Starting.."
    docker start $CONTAINER
    docker exec -it $CONTAINER bash
}

function build() {
    echo "Building.."
    docker build -t $IMAGE .
    docker run -dit -p 5432:5432 --name $CONTAINER $IMAGE
}

function prune() {
    echo "Pruning.."
    docker stop $CONTAINER
    docker rm $CONTAINER
}

if [[ -z $1 ]]; then
    echo "Pass either 'start' or 'build' as first argument."
    exit 0
fi

if [[ $1 == "start" ]]; then
    start
fi

if [[ $1 == "build" ]]; then
    build
fi

if [[ $1 == "prune" ]]; then
    prune
fi

if [[ $1 == "all" ]]; then
    prune
    build
    start
fi