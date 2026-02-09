import pandas as pd
import random
import time
from datetime import datetime
 
METRICS_FILE = "Data/metrics_stream.csv"
COST_FILE = "Data/cost_history_stream.csv"
VM_ID = "vm-101"
 
# timers
last_cost_time = 0
 
def generate_cpu():
    base = 30
    variation = random.uniform(-15, 25)
    return max(5, min(95, base + variation))
 
def generate_cost():
    return random.uniform(450, 550)
 
print("Starting data simulator...")
 
while True:
 
    current_time = time.time()
 
    # ---- Generate CPU metrics every minute ----
    metrics_row = {
        "timestamp": datetime.utcnow(),
        "vm_id": VM_ID,
        "cpu_usage_pct": round(generate_cpu(), 2)
    }
 
    pd.DataFrame([metrics_row]).to_csv(
        METRICS_FILE,
        mode="a",
        header=False,
        index=False
    )
 
    print("Metrics generated:", metrics_row)
 
    # ---- Generate cost once per hour ----
    if current_time - last_cost_time >= 3600:
        cost_row = {
            "month": datetime.utcnow().strftime("%Y-%m"),
            "vm_id": VM_ID,
            "monthly_cost": round(generate_cost(), 2)
        }
 
        pd.DataFrame([cost_row]).to_csv(
            COST_FILE,
            mode="a",
            header=False,
            index=False
        )
 
        print("Cost generated:", cost_row)
 
        last_cost_time = current_time
 
    time.sleep(60)