#!/bin/bash

MYSQL_USER=""
MYSQL_PASSWORD=""
MYSQL_HOST=""

-- query to show the databses
mysql -h "${MYSQL_HOST}" -u "${MYSQL_USER}" "-p${MYSQL_PASSWORD}" -e "SHOW DATABASES;"
