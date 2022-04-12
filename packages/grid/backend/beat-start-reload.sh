#! /usr/bin/env bash

echo "Running worker-start-reload.sh with RELEASE=${RELEASE}"

set -e

while [ ! -f /app/syft/setup.py ]
do
    echo "Waiting for syft folder to sync"
    sleep 1
done

pip install --user -e /app/syft[dev]

python /app/grid/backend_prestart.py

celery -A grid.periodic_tasks beat -l info --detach
watchmedo auto-restart --directory=/app --pattern=*.py --recursive -- celery -A grid.periodic_tasks worker -l info -Q celery -n beatworker.%h
