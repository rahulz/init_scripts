import os
import pdb
import sys

assets_path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "assets")
path = os.environ['PWD']
project_name = os.path.split(path)[-1]

if not os.path.exists('manage.py') or not os.path.isdir(project_name):
    raise Exception("Not a django directory")

# Main celery file
print("Writing celery.py")
core = open(os.path.join(assets_path, 'celery.py')).read().replace('{project_name}', project_name)
with open(os.path.join(project_name, 'celery.py'), 'w') as f:
    f.write(core)
print("Writing celery.py: DONE")

# Tasks file
print("Writing tasks")
tasks = open(os.path.join(assets_path, 'tasks.py')).read().replace('{project_name}', project_name)
pdb.set_trace()
for x in filter(lambda d: os.path.exists(d + '/urls.py'), filter(os.path.isdir, os.listdir('.'))):
    print(f"Writing {x}/task.py")
    with open(os.path.join(x, 'tasks.py'), 'w') as f:
        f.write(tasks)
print("Writing tasks: DONE")

# settings
print("Writing settings.py: DONE")
settings = open(os.path.join(assets_path, 'settings.py')).read().replace('{project_name}', project_name)
with open(os.path.join(project_name, 'settings.py'), 'a') as f:
    f.write(settings)

print("Writing settings.py: DONE")
