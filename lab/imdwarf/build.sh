#!/bin/bash

FIND_PATH="/c/repositories"
INCLUDE_FOLDER=$(find $FIND_PATH -wholename "*/TVT/cpp/include")
OUTPUT_FOLDER="output"

g++ -o imdwarf -I $INCLUDE_FOLDER imdwarf.c

rm -rf $OUTPUT_FOLDER
mkdir -p $OUTPUT_FOLDER
mkdir -p $OUTPUT_FOLDER/assets

mv imdwarf $OUTPUT_FOLDER
cp assets/* $OUTPUT_FOLDER/assets
