import pandas as pd

def load_vm_cost():
    df = pd.read_excel("Data/vm_cost.xlsx")
    df["monthly_cost"] = pd.to_numeric(df["monthly_cost"])
    return df


def load_cost_history():
    df = pd.read_csv("Data/cost_history_stream.csv")

    # Ensure correct column names if headers missing
    if "vm_id" not in df.columns:
        df.columns = ["month", "vm_id", "monthly_cost"]

    df["monthly_cost"] = pd.to_numeric(df["monthly_cost"])

    return df
