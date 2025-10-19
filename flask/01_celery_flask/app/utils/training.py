import random
import time
from enum import Enum, unique
from typing import Any, Dict


def mock_model_predict(input: str) -> Dict[str, str]:
    delay = random.randint(8, 15)
    time.sleep(delay)
    result = str(random.randint(100, 10000))
    output = {"input": input, "result": result}
    return output


@unique
class TrainingStatus(Enum):
    SUCCESS = "SUCCESS"
    PENDING = "PENDING"

    def __get__(self, *_: Any):
        return self.name
