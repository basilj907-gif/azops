import pandas as pd
 
def load_vm_config():
    return pd.read_excel("backend/data/vm_config.xlsx")