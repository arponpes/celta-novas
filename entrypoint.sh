#!/bin/sh

# Run migrations, wait for the database, and start the server
python3 manage.py migrate
python3 manage.py wait_for_db
python3 manage.py collectstatic
python3 manage.py runserver 0.0.0.0:8080
