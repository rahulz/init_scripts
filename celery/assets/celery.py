from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')

app = Celery('{project_name}')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    pass
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(10.0, test.s("helklo woller"), name='add every 10')

    # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    #sender.add_periodic_task(
    #    crontab(hour=17, minute=25),
    #    sync_all.s(), name="Sync users @ Every 21:00 Everyday"
    #)
    #
    # sender.add_periodic_task(
    #     crontab(hour=21, minute=00),
    #     send_summary.s(), name="Send summery @ Every 23:00 Everyday"
    # )

# sender.add_periodic_task(
#     crontab(hour=12, minute=22),
#     sync_events.s(), name="Sync events @ Every 1:00 Everyday"
# )
# sender.add_periodic_task(
#     crontab(hour=12, minute=22),
#     sync_projects.s(), name="Sync projects @ Every 1:00 Everyday"
# )
