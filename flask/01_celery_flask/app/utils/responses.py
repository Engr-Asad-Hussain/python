from typing import Any

from marshmallow.exceptions import ValidationError

from flask import Response, jsonify, make_response


def response(
    message: str | dict[str, Any],
    *,
    status_code: int = 200,
    data: Any = None,
    message_key: str = "message"
) -> Response:
    """
    Serialize the response.
    Args:
        - `message`: The message to be displayed in the response.
        - `message_key` (str): The default key of the message is message. Pass the keyward argument to change it.
        - `status_code` (int): The status code to be attach in the response.
        - `data` (Any): The response body needs to send.
    """

    body = {message_key: message, "status_code": status_code}
    if data is not None:
        body["data"] = data
    resp = make_response(jsonify(body))
    resp.status_code = status_code
    return resp


def raise_exc(error: Exception) -> Response:
    """
    Serialize the response based on the exceptions.
    Args:
        - `error` (Exception): The exception raised in the view funtion.
    """

    http_code = getattr(error, "http_code", 500)
    message = error.__str__()
    if isinstance(error, ValidationError):
        message = error.messages
    return response(message, status_code=http_code, message_key="error")
