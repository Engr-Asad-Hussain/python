from celery import Celery, Task
from flask import Flask
from typing import Any


def celery_init(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: Any, **kwargs: Any) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name)
    celery_app.Task = FlaskTask
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app
