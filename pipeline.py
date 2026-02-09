from ingestion1.metrics_loader import load_metrics
from ingestion1.config_loader import load_vm_config
from ingestion1.cost_loader import load_vm_cost, load_cost_history

from analytics.usageanalysis import analyze_usage
from analytics.rightsizing import recommend_rightsizing
from analytics.costoptimization import calculate_cost_impact
from analytics.prediction import predict_cost


def run_pipeline(vm_id):

    # ---------- Load data ----------
    metrics = load_metrics()
    config = load_vm_config()
    cost = load_vm_cost()
    cost_history = load_cost_history()

    # ---------- Validate VM exists ----------
    vm_metrics = metrics[metrics["vm_id"] == vm_id]
    if vm_metrics.empty:
        raise ValueError(f"Metrics not found for vm_id: {vm_id}")

    vm_config = config[config["vm_id"] == vm_id]
    if vm_config.empty:
        raise ValueError(f"VM config not found for vm_id: {vm_id}")

    vm_config = vm_config.iloc[0]

    # Ensure numeric types
    vcpu = float(vm_config["vcpu"])

    # ---------- Usage analysis ----------
    usage = analyze_usage(vm_metrics)

    cpu_p95 = float(usage["cpu_p95"])

    # ---------- Rightsizing ----------
    rightsizing = recommend_rightsizing(cpu_p95, vcpu)

    required_vcpu = float(rightsizing["required_vcpu"])

    # ---------- Cost lookup ----------
    cost_row = cost[cost["vm_size"] == vm_config["vm_size"]]
    if cost_row.empty:
        raise ValueError(f"Cost entry not found for vm_size: {vm_config['vm_size']}")

    current_cost = float(cost_row["monthly_cost"].values[0])

    optimized_cost = float(current_cost * (required_vcpu / vcpu))

    # ---------- Cost impact ----------
    cost_impact = calculate_cost_impact(current_cost, optimized_cost)

    # ---------- Historical prediction ----------
    vm_cost_history = cost_history[cost_history["vm_id"] == vm_id]

    prediction_base = predict_cost(vm_cost_history)

    predicted_current = float(prediction_base["predicted_cost_next_month"])

    optimized_ratio = optimized_cost / current_cost if current_cost else 1

    predicted_optimized = float(predicted_current * optimized_ratio)

    forecast_savings = float(predicted_current - predicted_optimized)

    # ---------- Final result ----------
    result = {
        "vm_id": vm_id,
        "usage": usage,
        "rightsizing": rightsizing,
        "current_cost": current_cost,
        "optimized_cost": optimized_cost,
        "cost_impact": cost_impact,
        "prediction": {
            "predicted_cost_without_optimization": predicted_current,
            "predicted_cost_with_optimization": predicted_optimized,
            "forecasted_monthly_savings": forecast_savings
        }
    }

    return result


if __name__ == "__main__":
    print(run_pipeline("vm-101"))
