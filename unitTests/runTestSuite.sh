#!/bin/bash
rm docker/dynamodb/shared-local-instance.db

pip install -r requirements.txt

docker pull amazon/dynamodb-local && docker-compose up & npm start & (sleep 5 && pytest && docker-compose down && npm stop)
