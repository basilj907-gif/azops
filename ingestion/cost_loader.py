import pandas as pd
 
def load_vm_cost():
    return pd.read_excel("Data/vm_cost.xlsx")
 
def load_cost_history():
    return pd.read_csv("Data/cost_history_stream.csv")