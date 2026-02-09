import pandas as pd
import random
import time
from datetime import datetime
import os

METRICS_FILE = "Data/metrics_stream.csv"
COST_FILE = "Data/cost_history_stream.csv"

VMS = {
    "vm-101": {"base_cpu": 35},
    "vm-102": {"base_cpu": 10},   # underutilized
    "vm-103": {"base_cpu": 75},   # highly utilized
    "vm-104": {"base_cpu": 50},   # moderate utilization
}

last_cost_time = 0

def generate_cpu(base):
    return max(5, min(95, base + random.uniform(-10, 15)))

def generate_cost():
    return random.uniform(450, 550)

while True:
    current_time = time.time()

    # ---- metrics for each VM ----
    for vm_id, config in VMS.items():
        row = {
            "timestamp": datetime.utcnow(),
            "vm_id": vm_id,
            "cpu_usage_pct": round(generate_cpu(config["base_cpu"]), 2)
        }

        header_needed = not os.path.exists(METRICS_FILE)

        pd.DataFrame([row]).to_csv(
            METRICS_FILE,
            mode="a",
            header=header_needed,
            index=False
        )

        print("Metrics:", row)

    # ---- cost history hourly ----
    if current_time - last_cost_time >= 3600:
        for vm_id in VMS:
            row = {
                "month": datetime.utcnow().strftime("%Y-%m"),
                "vm_id": vm_id,
                "monthly_cost": round(generate_cost(), 2)
            }

            header_needed = not os.path.exists(COST_FILE)

            pd.DataFrame([row]).to_csv(
                COST_FILE,
                mode="a",
                header=header_needed,
                index=False
            )

            print("Cost:", row)

        last_cost_time = current_time

    time.sleep(60)
