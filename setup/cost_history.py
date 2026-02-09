import pandas as pd
from datetime import datetime, timedelta
import random
import os

FILE_PATH = "Data/cost_history_stream.csv"

VMS = ["vm-101", "vm-102", "vm-103", "vm-104"]

rows = []

# create 6 months of historical cost data
for i in range(6):
    month = (datetime.utcnow() - timedelta(days=30*i)).strftime("%Y-%m")

    for vm in VMS:
        rows.append({
            "month": month,
            "vm_id": vm,
            "monthly_cost": round(random.uniform(450, 550), 2)
        })

df = pd.DataFrame(rows)

# overwrite existing file (for demo)
df.to_csv(FILE_PATH, index=False)

print("Cost history seeded successfully")
print("Rows created:", len(df))
