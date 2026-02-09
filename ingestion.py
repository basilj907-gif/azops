import pandas as pd
import os
 
def load_azure_metrics(file_path):
    """
    Load exported Azure Monitor InsightsMetrics data
    """
    df = pd.read_csv(file_path)
 
    # Filter CPU utilization metrics
    df = df[df["Name"] == "UtilizationPercentage"]
 
    # Rename columns to internal schema
    df = df.rename(columns={
        "TimeGenerated [UTC]": "timestamp",
        "Computer": "vm_id",
        "Val": "cpu_usage_pct"
    })
 
    df["timestamp"] = pd.to_datetime(df["timestamp"])
 
    return df[["timestamp", "vm_id", "cpu_usage_pct"]]
if __name__ == "__main__":
    df = load_azure_metrics("Data/processor.csv")
    print(df.head())
    print("Rows:", len(df))