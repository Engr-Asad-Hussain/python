from celery import shared_task
from celery.utils.log import get_task_logger

from app.predict import models
from app.utils import training


logger = get_task_logger(__name__)


@shared_task
def async_prediction(string: str, prediction_id: int):
    """
    Async task to process model training in background task.
    Args:
        - `string` (str): The input of the training model.
        - `prediction_id` (int): The prediction id used to update the model assets after completion.
    """

    data = training.mock_model_predict(string)
    models.update_status(prediction_id, data["result"])
