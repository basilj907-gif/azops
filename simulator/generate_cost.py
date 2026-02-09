import pandas as pd
import random
import time
from datetime import datetime
 
FILE_PATH = "Data/cost_history_stream.csv"
VM_ID = "vm-101"
 
while True:
    row = {
        "month": datetime.utcnow().strftime("%Y-%m"),
        "vm_id": VM_ID,
        "monthly_cost": random.uniform(450, 550)
    }
 
    pd.DataFrame([row]).to_csv(FILE_PATH, mode="a", header=False, index=False)
    print("Generated cost:", row)
 
    time.sleep(3600)