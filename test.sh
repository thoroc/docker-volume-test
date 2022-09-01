#!/bin/sh

echo "Cleaning up the output directories"
rm -fr export/
rm -fr include/

docker-compose build

docker-compose up

echo "listing files under ./export"
tree ./export

echo "listing files under ./include"
tree ./include

