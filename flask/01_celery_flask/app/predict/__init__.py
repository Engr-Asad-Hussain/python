from typing import Any

from app import db

from flask import Blueprint
from flask import current_app as app

bp = Blueprint("predict", __name__)


# @app.teardown_request
# def teardown_request(exceptions: Any = None):
#     db.close()
