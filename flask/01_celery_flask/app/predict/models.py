from typing import Any

from app import db
from app.exceptions import DoesNotExists
from app.predict import tasks
from app.utils.training import TrainingStatus


def save_prediction(result: str, *, is_completed: bool = True) -> int:
    try:
        sp = db.post(procedure="sde_addPrediction", arguments=(result, is_completed))
        db.save()
    except Exception as e:
        raise e
    else:
        return sp["prediction_id"]
    finally:
        db.close()


def get_prediction(prediction_id: int) -> dict[str, Any]:
    try:
        sp = db.get(procedure="sde_getPrediction", arguments=(prediction_id,))
    except DoesNotExists:
        raise DoesNotExists(f"Prediction({prediction_id}) not does not exists.")
    else:
        return {
            "predictionId": sp["prediction_id"],
            "output": {
                "predictionResult": sp["prediction_output"],
                "predictionStatus": (
                    TrainingStatus.SUCCESS
                    if bool(sp["is_completed"])
                    else TrainingStatus.PENDING
                ),
                "createdAt": sp["created_at"],
            },
        }
    finally:
        db.close()


def update_status(prediction_id: int, result: str) -> None:
    try:
        is_completed = True
        db.put(
            procedure="sde_updatePrediction",
            arguments=(prediction_id, result, is_completed),
        )
        db.save()
    except Exception as e:
        raise e
    finally:
        db.close()


def process_async(request_body: str) -> tuple[int, str]:
    prediction_id = save_prediction(result="", is_completed=False)
    task = tasks.async_prediction.delay(request_body, prediction_id)
    return prediction_id, task.status
