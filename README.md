# Website

## Commands

```commandline
docker-compose -f docker-compose.prod.yml up -d --build
```

```commandline
docker-compose -f docker-compose.prod.yml down -v
```

```commandline
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```

```commandline
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```
