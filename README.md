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

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/rajababu-code/QueueLess-AI.git
cd QueueLess-AI

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

### 4. Retrain the Random Forest model (optional)

```bash
python train_model.py
```

### Project Structure

QueueLess-AI/
│
├── app.py
├── predictor.py
├── train_model.py
├── queue_data.csv
├── queue_wait_model.joblib
├── requirements.txt
├── README.md
├── architecture.md
├── demo_script.md
├── project_report.md
├── SUBMISSION_CHECKLIST.md
└── QueueLess_AI_Project_Report.pdf

### Future scope
Real queue data, QR check-ins, sensors, live updates, mobile app, admin dashboard and continuous retraining.

**Author:** Raja Babu
