#!/usr/bin/env bash

container_name=django_postgres_side_project
docker exec -it $container_name /bin/bash

# 접속후 psql 접속은
# su postgres
# psql