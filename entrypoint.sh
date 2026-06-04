#!/bin/sh

set -e

echo "==> Running database migrations on persistent volume..."
python manage.py migrate --noinput

echo "==> Loading initial subjects fixtures..."
python manage.py loaddata subjects.json

echo "==> Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:8000 --workers 2 config.wsgi