from typing import Any
from flask import Blueprint, current_app as app
from app import db

bp = Blueprint("predict", __name__)


# @app.teardown_request
# def teardown_request(exceptions: Any = None):
#     db.close()
