#!/bin/sh

echo "Cleaning up the output directories"
rm -fr export/
rm -fr include/
rm -fr exclude/

docker-compose build

docker-compose up

echo ""
echo "> listing files under ./export"
tree ./export

echo ""
echo "> listing files under ./include"
tree ./include

echo ""
echo "> listing files under ./exclude"
tree ./exclude

echo ""
echo "> copying files from ./include to ./export/include"
cp -r ./include ./export/include

echo ""
echo "> copying files from ./exclude to ./export/exclude"
cp -r ./exclude ./export/exclude

echo ""
echo "> re-listing files under ./export"
tree ./export