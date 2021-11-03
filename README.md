# Website

## Commands

Build and start everything:
```commandline
docker-compose -f docker-compose.prod.yml up -d --build
```

Stop all services:
```commandline
docker-compose -f docker-compose.prod.yml down
```

Export updated `requirements.txt`, necessary whenever dependencies changed:
```commandline
poetry export -f requirements.txt --output requirements.txt
```

Redeploy Django app:
```commandline
sudo docker-compose -f docker-compose.prod.yml up -d --force-recreate --build web
```

### Manual management commands
```commandline
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```

```commandline
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

### Copying config files
Retrieve from server:
```commandline
scp -r princeton@princetonpy.org:/home/princeton/princetonpy.org/prod/{.env.prod.web,.env.prod.aws,.env.prod.db,.env.prod.nginx,.env.prod.proxy-companion} .
```

Transfer to server:
```commandline
scp -r $(pwd)/{.env.prod.web,.env.prod.aws,.env.prod.db,.env.prod.nginx,.env.prod.proxy-companion} princeton@princetonpy.org:/home/princeton/princetonpy.org/prod
scp -r $(pwd)/{.env.staging.aws,.env.staging.db,.env.staging.nginx,.env.staging.web,.env.staging.proxy-companion} princeton@princetonpy.org:/home/princeton/princetonpy.org/staging
```

### Importing users from CSV
Make sure file is copied to mounted app directory:
```commandline
scp -r princetonpy_subscriptions.csv user@host:/path
sudo docker-compose -f docker-compose.prod.yml run web sh
python manage.py subscriptions import ./princetonpy_subscriptions.csv
```

### Access DB
```commandline
sudo docker-compose -f docker-compose.prod.yml exec db psql -U postgres -W princetonpy_prod
select * from django_site;
```