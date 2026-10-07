from pathlib import Path
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ROOT = Path(__file__).parent

FEATURES = [
    "people_in_queue",
    "avg_service_time_min",
    "hour",
    "day_of_week",
    "arrival_rate_per_min",
    "counter_efficiency"
]

DATA_PATH = ROOT / "queue_data.csv"
MODEL_PATH = ROOT / "queue_wait_model.joblib"

data = pd.read_csv(DATA_PATH)

X_train, X_test, y_train, y_test = train_test_split(
    data[FEATURES],
    data["waiting_time_minutes"],
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=250,
    max_depth=12,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)

joblib.dump(
    {
        "model": model,
        "features": FEATURES
    },
    MODEL_PATH
)

print("Model saved to:", MODEL_PATH)
