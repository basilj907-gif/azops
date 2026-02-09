import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def predict_cpu_usage(df, periods=10, model_type='linear'):
    """
    Predict future CPU usage based on historical data
    
    Args:
        df: DataFrame with 'timestamp' and 'cpu_usage_pct' columns
        periods: Number of time periods to predict
        model_type: 'linear' or 'polynomial'
    
    Returns:
        Dictionary with predictions and model info
    """
    
    # Sort by timestamp
    df = df.sort_values('timestamp').reset_index(drop=True)
    
    # Convert timestamp to numeric (days since first timestamp)
    time_numeric = np.arange(len(df)).reshape(-1, 1)
    cpu_values = df["cpu_usage_pct"].values
    
    # Train model
    if model_type == 'polynomial':
        poly = PolynomialFeatures(degree=2)
        X = poly.fit_transform(time_numeric)
        model = LinearRegression()
        model.fit(X, cpu_values)
    else:  # linear
        model = LinearRegression()
        model.fit(time_numeric, cpu_values)
    
    # Make predictions for future periods
    future_time = np.arange(len(df), len(df) + periods).reshape(-1, 1)
    
    if model_type == 'polynomial':
        future_X = poly.transform(future_time)
        predictions = model.predict(future_X)
    else:
        predictions = model.predict(future_time)
    
    # Ensure predictions are within reasonable bounds (0-100%)
    predictions = np.clip(predictions, 0, 100)
    
    # Calculate model performance on historical data
    if model_type == 'polynomial':
        train_pred = model.predict(X)
    else:
        train_pred = model.predict(time_numeric)
    
    mse = np.mean((cpu_values - train_pred) ** 2)
    rmse = np.sqrt(mse)
    mae = np.mean(np.abs(cpu_values - train_pred))
    
    return {
        "predictions": predictions.tolist(),
        "periods": periods,
        "model_type": model_type,
        "rmse": float(rmse),
        "mae": float(mae),
        "avg_predicted_cpu": float(np.mean(predictions)),
        "trend": "increasing" if predictions[-1] > np.mean(cpu_values) else "decreasing"
    }

if __name__ == "__main__":
    from ingestion import load_azure_metrics
    
    df = load_azure_metrics("Data/processor.csv")
    
    # Linear prediction
    linear_pred = predict_cpu_usage(df, periods=20, model_type='linear')
    print("Linear Prediction:")
    print(linear_pred)
    
    print("\n" + "="*50 + "\n")
    
    # Polynomial prediction
    poly_pred = predict_cpu_usage(df, periods=20, model_type='polynomial')
    print("Polynomial Prediction:")
    print(poly_pred)
