# FastAPI + SQLModel + Alembic

## Quick start

```sh
docker-compose up --build
```
To start a development server, it will hot-reload similar to that of a usual uvicorn server.

NOTE: The development server's database is **persistent**. If you want to clear the data, you need to call:

```sh
docker-compose down -v
```

### Migrations

to do a migration you can call 
```
./scripts/create_migration.sh <migration name>
```

> NOTE: Migration names should always be snake case

Migrations should be reflected also with a reference in the 'migrations/README'

### Tests

```sh
./scripts/test.sh
```

To run our tests, there should never be a commit with unexpected failing tests

NOTE: The images may not be built before testing. If unsure, run `docker-compose build`.
