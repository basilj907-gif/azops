import numpy as np
 
def analyze_cpu_usage(df):
    """
    Calculate CPU P50 and P95
    """
    cpu_values = df["cpu_usage_pct"].values
 
    cpu_p50 = float(np.percentile(cpu_values, 50))
    cpu_p95 = float(np.percentile(cpu_values, 95))
 
    workload_pattern = (
        "steady" if (cpu_p95 - cpu_p50) < 20 else "spiky"
    )
 
    return {
        "cpu_p50": cpu_p50,
        "cpu_p95": cpu_p95,
        "workload_pattern": workload_pattern
    }

if __name__ == "__main__":
    from ingestion import load_azure_metrics
 
    df = load_azure_metrics("Data/processor.csv")
    result = analyze_cpu_usage(df)
 
    print(result)