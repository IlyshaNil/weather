#!/bin/bash

echo "Migrate the Database"

while ! python src/manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done

while ! python src/manage.py collectstatic --noinput  2>&1; do
   sleep 3
done

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_USERNAME
fi

exec "$@"