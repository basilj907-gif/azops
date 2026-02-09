import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "Data", "vm_config.xlsx")

data = [
    {"vm_id": "vm-101", "vm_size": "D8s_v5", "vcpu": 8, "memory_gb": 32, "region": "eastus"},
    {"vm_id": "vm-102", "vm_size": "D8s_v5", "vcpu": 8, "memory_gb": 32, "region": "eastus"},
    {"vm_id": "vm-103", "vm_size": "D4s_v5", "vcpu": 4, "memory_gb": 16, "region": "eastus"},
    {"vm_id": "vm-104", "vm_size": "D16s_v5", "vcpu": 16, "memory_gb": 64, "region": "eastus"},
]

df = pd.DataFrame(data)

df.to_excel(file_path, index=False)

print("vm_config.xlsx updated at:", file_path)
