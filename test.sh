#!/bin/sh

docker-compose build

docker-compose up

echo "listing files under ./export"
tree ./export

echo "listing files under ./include"
tree ./include

