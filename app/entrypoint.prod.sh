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

if [ -n "$UID" ] && [ -n "$GID" ]; then
    usermod -u "$UID" app
    groupmod -g "$GID" app
    chown -R "$UID":"$GID" "$HOME"
fi

exec "$@"
