from ingestion import load_azure_metrics
from usage import analyze_cpu_usage
from rightsizing import recommend_rightsizing
from cost_saving import estimate_cost_savings
from prediction import predict_cpu_usage
 
# Load data
df = load_azure_metrics("Data/processor.csv")
 
# Analyze usage
usage = analyze_cpu_usage(df)

# Predict future CPU usage
prediction = predict_cpu_usage(df, periods=20, model_type='polynomial')
 
# Rightsizing (example: current VM = 8 vCPU)
rightsizing = recommend_rightsizing(
    cpu_p95=usage["cpu_p95"],
    current_vcpu=8
)
 
# Cost estimation (mock values)
cost = estimate_cost_savings(
    current_cost=500,
    new_cost=280
)
 
# Final output
output = {
    "usage": usage,
    "prediction": prediction,
    "rightsizing": rightsizing,
    "cost_impact": cost
}
 
print(output)