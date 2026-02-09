import pandas as pd

def load_vm_config():
    df = pd.read_excel("Data/vm_config.xlsx")

    df["vcpu"] = pd.to_numeric(df["vcpu"])
    df["memory_gb"] = pd.to_numeric(df["memory_gb"])

    return df
