
from .celery import app as celery_app
__all__ = ('celery_app',)

<<<<<<< HEAD
=======


#-------------comand line for running cellery worker-----------

# celery -A busbookingApp worker -l INFO

#-------------comand line for running cellery_beat-----------

# celery -A busbookingApp beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
>>>>>>> 6e77fe80d5e4e6de116c3b49e9266fea373e1ce4
