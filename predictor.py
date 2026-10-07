import joblib, pandas as pd
from pathlib import Path
BUNDLE=joblib.load(Path(__file__).parent/'models/queue_wait_model.joblib')
def predict_wait(people_in_queue,avg_service_time_min,hour,day_of_week,arrival_rate_per_min,counter_efficiency):
    row=pd.DataFrame([locals()])
    return float(BUNDLE['model'].predict(row[BUNDLE['features']])[0])
