#!/bin/sh

set -e

echo "==> Running database migrations on persistent volume..."
python manage.py migrate --noinput

echo "==> Loading initial subjects fixtures..."
python manage.py loaddata subjects.json

echo "==> Starting Daphne ASGI server..."
exec daphne -b 0.0.0.0 -p 8000 config.asgi:application