#!/bin/sh

service_name=runtime-ff-db-1
database=foo
user=postgres

psql -h $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $service_name) -p 5432 -U $user -d $database
