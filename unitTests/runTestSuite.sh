#!/bin/bash
rm docker/dynamodb/shared-local-instance.db

docker-compose up & npm start & (sleep 5 && pytest && docker-compose down && npm stop)