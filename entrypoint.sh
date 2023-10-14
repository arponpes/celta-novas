#!/bin/sh

# Run migrations, wait for the database, and start the server
python3 manage.py migrate
python3 manage.py wait_for_db
python3 manage.py collectstatic
celery -A celta_novas beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler --detach
celery -A celta_novas worker -l INFO -n default_worker --detach
python3 manage.py runserver 0.0.0.0:8080
