import os
import dotenv

from datetime import datetime
from functools import partial

dotenv.load_dotenv()


class Config:
    # Application Configurations
    APP_HOST           = "0.0.0.0"
    APP_PORT           = 8080
    APP_DEBUG          = bool(os.getenv("FLASK_DEBUG"))
    APP_START_TIME     = datetime.utcnow()

    # Celery Configurations
    CELERY_BROKER      = os.getenv("CELERY_BROKER")
    CELERY_BACKEND     = os.getenv("CELERY_BACKEND")


class Development(Config):
    # Database Configurations
    DATABASE           = os.getenv("DATABASE")
    DB_USERNAME        = os.getenv("DB_USERNAME")
    DB_PASSWORD        = os.getenv("DB_PASSWORD")
    DB_HOST            = os.getenv("DB_HOST")
    DB_PORT            = os.getenv("DB_PORT")


class Production(Config):
    # Database Configurations
    DATABASE           = os.getenv("DATABASE")
    DB_USERNAME        = os.getenv("DB_USERNAME")
    DB_PASSWORD        = os.getenv("DB_PASSWORD")
    DB_HOST            = os.getenv("DB_HOST")
    DB_PORT            = os.getenv("DB_PORT")


def _check_app(cls: type[Development | Production]) -> type[Development | Production]:
    for obj in (Config, cls):
        for key, value in vars(obj).items():
            if key.startswith("__"):
                continue
            if value is None:
                raise RuntimeError(
                    f"Missing Environmental Variable(s) | Variable: {key}={value}"
                )
    return cls


Dev = partial(_check_app, Development)
Prod = partial(_check_app, Production)
