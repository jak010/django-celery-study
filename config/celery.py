from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery('django-note-project', broker='amqp://guest:guest@localhost/')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.update(timezone='Asia/seoul')

app.conf.beat_schedule = {
    'test': {
        'task': 'apps.tasks.add',
        'schedule': crontab(),
        'args': (1, 1)
    }
}
