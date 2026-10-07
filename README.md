# QueueLess AI 🚦
## Intelligent Waiting-Time Prediction & Queue Optimization

**Logic League – Ideathon | Galgotias University**

**Theme:** AI/ML → **Small / Efficient AI**

QueueLess AI predicts expected waiting time at service counters and recommends the queue with the lowest predicted wait.

### Problem
A shorter queue is not always faster because service speed, arrival rate and counter efficiency vary.

### AI solution
A lightweight **Random Forest Regression** model uses queue length, average service time, hour, day of week, arrival rate and counter efficiency.

### Prototype metrics
On the included **synthetic** test dataset:
- MAE: **1.85 minutes**
- RMSE: **2.60 minutes**
- R²: **0.976**

These are prototype metrics only, not real-world accuracy.

### Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Retrain
```bash
python train_model.py
```

### Structure
- `app.py` — interactive Streamlit demo
- `predictor.py` — prediction function
- `train_model.py` — model training
- `data/queue_data.csv` — synthetic dataset
- `models/queue_wait_model.joblib` — trained model
- `docs/` — report, architecture, demo script, checklist

### Future scope
Real queue data, QR check-ins, sensors, live updates, mobile app, admin dashboard and continuous retraining.

**Author:** Raja Babu
