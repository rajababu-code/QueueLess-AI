import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(_file_).parent / "queue_wait_model.joblib"

BUNDLE = joblib.load(MODEL_PATH)


def predict_wait(
    people_in_queue,
    avg_service_time_min,
    hour,
    day_of_week,
    arrival_rate_per_min,
    counter_efficiency
):
    row = pd.DataFrame([{
        "people_in_queue": people_in_queue,
        "avg_service_time_min": avg_service_time_min,
        "hour": hour,
        "day_of_week": day_of_week,
        "arrival_rate_per_min": arrival_rate_per_min,
        "counter_efficiency": counter_efficiency
    }])

    return float(
        BUNDLE["model"].predict(row[BUNDLE["features"]])[0]
    )
