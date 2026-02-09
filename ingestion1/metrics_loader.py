import pandas as pd

def load_metrics():
    df = pd.read_csv(
        "Data/metrics_stream.csv",
        names=["timestamp", "vm_id", "cpu_usage_pct"]
    )

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df
