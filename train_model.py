from pathlib import Path
import pandas as pd, joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
ROOT=Path(__file__).parent
F=['people_in_queue','avg_service_time_min','hour','day_of_week','arrival_rate_per_min','counter_efficiency']
d=pd.read_csv(ROOT/'data/queue_data.csv'); a,b,c,e=train_test_split(d[F],d.waiting_time_minutes,test_size=.2,random_state=42)
m=RandomForestRegressor(n_estimators=250,max_depth=12,random_state=42,n_jobs=-1);m.fit(a,c);p=m.predict(b)
print('MAE',mean_absolute_error(e,p));print('RMSE',mean_squared_error(e,p)**.5);print('R2',r2_score(e,p))
joblib.dump({'model':m,'features':F},ROOT/'models/queue_wait_model.joblib')
