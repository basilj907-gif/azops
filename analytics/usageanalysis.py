import numpy as np
 
def analyze_usage(df):
    cpu_values = df["cpu_usage_pct"].values
 
    return {
        "cpu_p50": float(np.percentile(cpu_values, 50)),
        "cpu_p95": float(np.percentile(cpu_values, 95))
    }