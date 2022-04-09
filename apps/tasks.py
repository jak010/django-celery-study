from __future__ import absolute_import, unicode_literals

from config.celery import app
from celery import shared_task


@app.task
def test_function(x, y):
    return x + y


# beat schedule
@shared_task()
def test():
    data = {"task": 1}
    return data
