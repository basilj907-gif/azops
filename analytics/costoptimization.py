def calculate_cost_impact(current_cost, new_cost):
    savings = current_cost - new_cost
    return {
        "estimated_monthly_savings": savings,
        "savings_percent": round((savings/current_cost)*100, 2)
    }