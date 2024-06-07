#!/bin/sh

docker-compose up db migrater -d

DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/foo

env PYTHONPATH="$PYTHONPATH:$PWD:/app"\
	DATABASE_URL="$DATABASE_URL" \
	poetry run pytest
