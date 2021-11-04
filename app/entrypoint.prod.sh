#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py collectstatic -c --noinput
python manage.py makemigrations
python manage.py migrate

if [ "$1" = 'hypercorn princetonpy.asgi:application --bind 0.0.0.0:8000' ]; then
  cron
  crontab -r
  echo -n "" | crontab -
  python manage.py crontab add
fi

exec "$@"
