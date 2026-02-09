from ingestion.metrics_loader import load_metrics
from ingestion.config_loader import load_vm_config
from ingestion.cost_loader import load_vm_cost, load_cost_history
from analytics.usage_analysis import analyze_usage
from analytics.rightsizing import recommend_rightsizing
from analytics.cost_optimization import calculate_cost_impact
from analytics.prediction import predict_cost
 
def run_pipeline(vm_id):
 
    metrics = load_metrics()
    config = load_vm_config()
    cost = load_vm_cost()
    cost_history = load_cost_history()
 
    vm_metrics = metrics[metrics["vm_id"] == vm_id]
    vm_config = config[config["vm_id"] == vm_id].iloc[0]
 
    usage = analyze_usage(vm_metrics)
 
    rightsizing = recommend_rightsizing(
        usage["cpu_p95"],
        vm_config["vcpu"]
    )
 
    current_cost = cost[cost["vm_size"] == vm_config["vm_size"]]["monthly_cost"].values[0]
    optimized_cost = current_cost * (rightsizing["required_vcpu"]/vm_config["vcpu"])
 
    cost_impact = calculate_cost_impact(current_cost, optimized_cost)
 
    vm_cost_history = cost_history[cost_history["vm_id"] == vm_id]
    prediction = predict_cost(vm_cost_history)
 
    return {
        "vm_id": vm_id,
        "usage": usage,
        "rightsizing": rightsizing,
        "cost_impact": cost_impact,
        "prediction": prediction
    }