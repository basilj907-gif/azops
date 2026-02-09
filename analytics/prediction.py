import numpy as np
 
def predict_cost(cost_df):
    y = cost_df["monthly_cost"].values
    x = np.arange(len(y))
 
    slope, intercept = np.polyfit(x, y, 1)
    predicted = slope*(len(y)) + intercept
 
    return {"predicted_cost_next_month": float(round(predicted,2))}