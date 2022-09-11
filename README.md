# Website

## Commands

Build and start everything:
```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

Stop all services:
```bash
docker-compose -f docker-compose.prod.yml down
```

Export updated `requirements.txt`, necessary whenever dependencies changed:
```bash
poetry export -f requirements.txt --output requirements.txt
```

Redeploy Django app:
```bash
sudo docker-compose -f docker-compose.prod.yml up -d --force-recreate --build web
```

### Manual management commands
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```

```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

### Copying config files
Retrieve from server:
```bash
scp -r princeton@princetonpy.org:/home/princeton/princetonpy.org/prod/{.env.prod.web,.env.prod.aws,.env.prod.db,.env.prod.nginx,.env.prod.proxy-companion} .
```

Transfer to server:
```bash
scp -r $(pwd)/{.env.prod.web,.env.prod.aws,.env.prod.db,.env.prod.nginx,.env.prod.proxy-companion} princeton@princetonpy.org:/home/princeton/princetonpy.org/prod
scp -r $(pwd)/{.env.staging.aws,.env.staging.db,.env.staging.nginx,.env.staging.web,.env.staging.proxy-companion} princeton@princetonpy.org:/home/princeton/princetonpy.org/staging
```

### Importing users from CSV
Make sure file is copied to mounted app directory:
```bash
scp -r princetonpy_subscriptions.csv user@host:/path
sudo docker-compose -f docker-compose.prod.yml run web sh
python manage.py subscriptions import ./princetonpy_subscriptions.csv
```

### Access DB
```bash
sudo docker-compose -f docker-compose.prod.yml exec db psql -U postgres -W princetonpy_prod
# select * from django_site;
```


### Working with backup files
```bash
sudo docker-compose -f docker-compose.prod.yml run cron ls -la /prod_backup/subscribers
sudo docker container ls
# get hash from CONTAINER ID column
sudo docker cp fc95ab44a580:/prod_backup .
```

### Manual Django shell updates

In server:
```bash
sudo -E docker compose -f docker-compose.prod.yml run web sh
```

In container:
```bash
python manage.py shell
```

And then in Django shell:
```python
import dateutil
from datetime import datetime

from meetings.models import Meeting

delta = dateutil.relativedelta.relativedelta(months=2)
before_date = datetime.now(tz=dateutil.tz.gettz("America/New_York")) - delta

# returns queryset
meeting_qs = Meeting.objects.filter(date__lte=before_date)
meeting_qs.update(tba=False)
```
