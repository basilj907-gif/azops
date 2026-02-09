import pandas as pd
 
def load_metrics():
    df = pd.read_csv("backend/data/metrics_stream.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df