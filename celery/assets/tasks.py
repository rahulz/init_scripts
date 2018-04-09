from __future__ import absolute_import, unicode_literals

from django.apps import apps
from {project_name} import settings

app = Celery('{project_name}')


#@app.task()
#def task():
#   User = apps.get_model('core.User')
