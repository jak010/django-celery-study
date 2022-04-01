from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

BROKER_URL = "amqp://guest:guest@localhost"

app = Celery('django-note-project',
             broker=BROKER_URL
             )
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.update(timezone='Asia/seoul')

app.conf.beat_schedule = {
    'test': {
        'task': 'apps.tasks.test',
        'schedule': 1,
        'args': (1,)
    }
}

import kombu

with app.pool.acquire(block=True) as conn:
    exchange = kombu.Exchange(
        name=BROKER_URL + "/task", type="topic", durable=True, channel=conn
    )
    exchange.declare()

    queue = kombu.Queue(
        name="my_queue",
        exchange=exchange,
        routing_key="my_queue.#",
        channel=conn,
    )
    queue.declare()
