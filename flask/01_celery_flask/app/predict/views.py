from flask import request

from app.exceptions import BadRequest
from app.predict import bp, models
from app.utils import training, schema
from app.utils.training import TrainingStatus
from app.utils.parser import parse_header
from app.utils.responses import response, raise_exc


@bp.route("/predict", methods=["POST"])
@parse_header
def predict(async_mode: bool):
    request_body = request.json
    try:
        # Schema Validations
        validator = schema.AddPrediction()
        payload = validator.inspect(request_body)
        string = payload["input"]

        if async_mode is False:
            data = training.mock_model_predict(string)
            prediction_id = models.save_prediction(data["result"])
            resp_body = {
                "string": string,
                "predictionId": prediction_id,
                "predictionStatus": TrainingStatus.SUCCESS,
                "predictionResult": data["result"],
            }
            return response("Prediction has been completed.", data=resp_body)
        else:
            prediction_id, status = models.process_async(string)
            resp_body = {
                "string": string,
                "predictionId": prediction_id,
                "predictionStatus": status,
            }
            return response(
                "Request received. Processing asynchronously.",
                data=resp_body,
                status_code=202,
            )

    except Exception as err:
        return raise_exc(err)


@bp.route("/predict/<int:prediction_id>", methods=["GET"])
def predict_detail(prediction_id: int):
    try:
        resp_body = models.get_prediction(prediction_id)
        if resp_body["output"]["predictionStatus"] == TrainingStatus.PENDING:
            raise BadRequest("Prediction is still being processed.")

    except Exception as err:
        return raise_exc(err)

    return response("Fetch the prediction.", data=resp_body)
