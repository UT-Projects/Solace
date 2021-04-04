#!/bin/bash
rm docker/dynamodb/shared-local-instance.db

echo Installing python modules

pip install -r requirements.txt

echo pulling dynamodb image

docker pull amazon/dynamodb-local

echo Iniatliazing...

docker-compose up & nyc start & (sleep 5 && pytest && docker-compose down && npm stop)
