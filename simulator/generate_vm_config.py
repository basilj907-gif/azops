import pandas as pd

data = [
    {"vm_id": "vm-101", "vm_size": "D8s_v5", "vcpu": 8, "memory_gb": 32, "region": "eastus"},
    {"vm_id": "vm-102", "vm_size": "D4s_v5", "vcpu": 4, "memory_gb": 16, "region": "eastus"}
]

df = pd.DataFrame(data)
df.to_excel("Data/vm_config.xlsx", index=False)

print("vm_config.xlsx created")