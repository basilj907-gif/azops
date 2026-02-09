def estimate_cost_savings(current_cost, new_cost):
    savings = current_cost - new_cost
    savings_percent = (savings / current_cost) * 100 if current_cost else 0
 
    return {
        "current_monthly_cost": current_cost,
        "recommended_monthly_cost": new_cost,
        "estimated_monthly_savings": savings,
        "savings_percent": round(savings_percent, 2)
    }

if __name__ == "__main__":
    result = estimate_cost_savings(500, 280)
    print(result)