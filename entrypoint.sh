#!/bin/sh

set -e

echo "==> Running database migrations on persistent volume..."
python manage.py migrate --noinput

echo "==> Loading initial full_data fixtures..."
python manage.py loaddata full_data.json

echo "==> Starting Daphne ASGI server..."
exec daphne -b 0.0.0.0 -p 8000 config.asgi:application