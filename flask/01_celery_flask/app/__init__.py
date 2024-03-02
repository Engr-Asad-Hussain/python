from datetime import datetime
from flask import Flask

from app.utils.responses import response
from app.database import Database
from app.celery_settings import celery_init


db = Database()


def create_app(settings: object):
    app = Flask(__name__)
    app.config.from_object(settings)
    db.init_app(app)
    app.config.from_mapping(
        CELERY=dict(
            broker_url=app.config["CELERY_BROKER"],
            result_backend=app.config["CELERY_BACKEND"],
            task_ignore_result=True,
        ),
    )
    celery = celery_init(app)

    with app.app_context():
        from app.predict.views import bp

        app.register_blueprint(bp)

        @app.route("/health", methods=["GET"])
        def health_check():
            resp_body = {
                "currentTime": datetime.utcnow(),
                "appStartTIme": app.config["APP_START_TIME"],
            }
            return response("Application is up.", data=resp_body)

        return app, celery
