import pandas as pd
import random
import time
from datetime import datetime
 
FILE_PATH = "Data/metrics_stream.csv"
VM_ID = "vm-101"
 
def generate_cpu():
    base = 30
    variation = random.uniform(-15, 25)
    return max(5, min(95, base + variation))
 
while True:
    row = {
        "timestamp": datetime.utcnow(),
        "vm_id": VM_ID,
        "cpu_usage_pct": round(generate_cpu(), 2)
    }
 
    pd.DataFrame([row]).to_csv(FILE_PATH, mode="a", header=False, index=False)
    print("Generated metrics:", row)
 
    time.sleep(60)