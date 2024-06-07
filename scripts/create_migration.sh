#!/bin/sh

if [ -z "$1" ]; then
  echo "Usage: $0 <migration_message>"
  exit 1
fi

# Run the migration service to create a new migration
docker-compose run --rm migration alembic revision --autogenerate -m "$1"
