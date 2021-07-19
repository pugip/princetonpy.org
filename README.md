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

```commandline
poetry export -f requirements.txt --output requirements.txt
```

Redeploy the Django server (in prod):
> This avoids redeploying the proxy containers that request certs.
> 
> If you exceed the cert request limit, Let's Encrypt rejects prod cert requests for a week or so.
```commandline
sudo docker-compose -f docker-compose.prod.yml up -d --force-recreate --build web
```