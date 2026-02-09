import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from Trash.ingestion import load_azure_metrics
from Trash.prediction import predict_cpu_usage

def plot_prediction(df, periods=20, model_type='polynomial'):
    """
    Plot actual CPU usage vs predicted CPU usage with better visualization
    """
    
    # Sort by timestamp
    df = df.sort_values('timestamp').reset_index(drop=True)
    
    # Get predictions
    prediction = predict_cpu_usage(df, periods=periods, model_type=model_type)
    
    # Create figure with 3 subplots
    fig = plt.figure(figsize=(16, 12))
    
    # ===== SUBPLOT 1: Combined view with clear separation =====
    ax1 = plt.subplot(3, 1, 1)
    
    actual_indices = np.arange(len(df))
    predicted_indices = np.arange(len(df), len(df) + periods)
    
    # Plot actual data
    ax1.plot(actual_indices, df["cpu_usage_pct"].values, 
            label='Actual CPU Usage', marker='o', linewidth=2.5, markersize=5, 
            color='#2E86AB', zorder=3)
    ax1.fill_between(actual_indices, df["cpu_usage_pct"].values, alpha=0.2, color='#2E86AB')
    
    # Plot predicted data
    ax1.plot(predicted_indices, prediction['predictions'], 
            label='Predicted CPU Usage', marker='s', linewidth=2.5, markersize=5, 
            color='#A23B72', linestyle='--', zorder=3)
    ax1.fill_between(predicted_indices, prediction['predictions'], alpha=0.2, color='#A23B72')
    
    # Add vertical separator
    ax1.axvline(x=len(df)-0.5, color='black', linestyle='--', linewidth=2, alpha=0.5)
    ax1.text(len(df)-0.5, ax1.get_ylim()[1]*0.98, '  Forecast Begins', 
            fontsize=11, ha='left', va='top', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))
    
    ax1.set_xlabel('Time Period', fontsize=12, fontweight='bold')
    ax1.set_ylabel('CPU Usage (%)', fontsize=12, fontweight='bold')
    ax1.set_title('CPU Usage: Actual vs Predicted (Combined View)', fontsize=13, fontweight='bold')
    ax1.legend(fontsize=11, loc='upper right', framealpha=0.95)
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # ===== SUBPLOT 2: Actual data only =====
    ax2 = plt.subplot(3, 1, 2)
    ax2.plot(actual_indices, df["cpu_usage_pct"].values, 
            color='#2E86AB', marker='o', linewidth=2.5, markersize=5, label='Actual Data')
    ax2.fill_between(actual_indices, df["cpu_usage_pct"].values, alpha=0.3, color='#2E86AB')
    
    # Add statistics for actual data
    actual_mean = df["cpu_usage_pct"].mean()
    actual_max = df["cpu_usage_pct"].max()
    actual_min = df["cpu_usage_pct"].min()
    
    ax2.axhline(y=actual_mean, color='green', linestyle='--', linewidth=2, label=f'Mean: {actual_mean:.2f}%')
    
    ax2.set_xlabel('Time Period', fontsize=12, fontweight='bold')
    ax2.set_ylabel('CPU Usage (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Historical Actual CPU Usage', fontsize=13, fontweight='bold')
    ax2.legend(fontsize=11, loc='upper right', framealpha=0.95)
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    # Add stats box for actual
    stats_actual = f"Data Points: {len(df)}\nMean: {actual_mean:.4f}%\nMax: {actual_max:.4f}%\nMin: {actual_min:.4f}%"
    ax2.text(0.02, 0.98, stats_actual, transform=ax2.transAxes, 
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    # ===== SUBPLOT 3: Predicted data only =====
    ax3 = plt.subplot(3, 1, 3)
    ax3.plot(predicted_indices, prediction['predictions'], 
            color='#A23B72', marker='s', linewidth=2.5, markersize=5, 
            linestyle=':', label='Predicted Data')
    ax3.fill_between(predicted_indices, prediction['predictions'], alpha=0.3, color='#A23B72')
    
    # Add statistics for predictions
    pred_mean = np.mean(prediction['predictions'])
    pred_max = np.max(prediction['predictions'])
    pred_min = np.min(prediction['predictions'])
    
    ax3.axhline(y=pred_mean, color='orange', linestyle=':', linewidth=2, label=f'Mean: {pred_mean:.2f}%')
    
    ax3.set_xlabel('Time Period', fontsize=12, fontweight='bold')
    ax3.set_ylabel('CPU Usage (%)', fontsize=12, fontweight='bold')
    ax3.set_title(f'Predicted CPU Usage ({periods} periods ahead)', fontsize=13, fontweight='bold')
    ax3.legend(fontsize=11, loc='upper right', framealpha=0.95)
    ax3.grid(True, alpha=0.3, linestyle='--')
    
    # Add stats box for predictions
    stats_pred = f"Periods: {periods}\nModel: {model_type.capitalize()}\nMean: {pred_mean:.4f}%\n"
    stats_pred += f"Max: {pred_max:.4f}%\nMin: {pred_min:.4f}%\nTrend: {prediction['trend'].capitalize()}"
    ax3.text(0.02, 0.98, stats_pred, transform=ax3.transAxes, 
            fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='#FFE5CC', alpha=0.7))
    
    # Add model metrics box
    metrics_text = f"RMSE: {prediction['rmse']:.4f}\nMAE: {prediction['mae']:.4f}"
    ax3.text(0.98, 0.02, metrics_text, transform=ax3.transAxes, 
            fontsize=10, verticalalignment='bottom', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('cpu_prediction_plot.png', dpi=300, bbox_inches='tight')
    print("✓ Graph saved as 'cpu_prediction_plot.png'")

if __name__ == "__main__":
    df = load_azure_metrics("Data/processor.csv")
    plot_prediction(df, periods=20, model_type='polynomial')
