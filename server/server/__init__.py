
from .celery import app as celery_app
__all__ = ('celery_app',)



#-------------comand line for running cellery worker-----------

# celery -A busbookingApp worker -l INFO

#-------------comand line for running cellery_beat-----------

# celery -A busbookingApp beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler