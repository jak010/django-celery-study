from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

BROKER_URL = "amqp://root:1234@localhost"

app = Celery('django-note-project',
             backend="rpc://",
             broker=BROKER_URL
             )
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.update(
    BROKER_URL=BROKER_URL,
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    timezone='Asia/seoul',

    # CELERY BEAT 를 통해 반복적으로 데이터를 처리할 수 있다
    CELERYBEAT_SCHEDULE={
        'test': {
            'task': 'apps.tasks.test',
            'schedule': 0.1,
            'args': ()
        }
    }

)
