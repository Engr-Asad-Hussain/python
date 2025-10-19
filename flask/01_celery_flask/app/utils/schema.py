from typing import Any

from marshmallow import Schema, fields, validate


class Validator(Schema):
    STR_001 = 1
    STR_256 = 256

    def inspect(self, payload: Any) -> dict[str, Any]:
        return super().load(payload)


class AddPrediction(Validator):
    input = fields.String(
        required=True,
        validate=validate.Length(min=Validator.STR_001, max=Validator.STR_256),
    )
