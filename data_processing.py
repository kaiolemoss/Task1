from analysis import (
    calculate_statistics, calculate_differences, identify_anomalies,
    calculate_correlation, daily_percentage_comparison, sales_distribution,
    calculate_daily_percent_change, calculate_moving_averages
)

def process_data(df):
    df = calculate_differences(df)
    df = calculate_daily_percent_change(df)
    df = calculate_moving_averages(df)
    return df

def analyze_data(df):
    stats = calculate_statistics(df)
    anomalies = identify_anomalies(df)
    correlation_matrix = calculate_correlation(df)
    daily_comparison = daily_percentage_comparison(df)
    sales_dist = sales_distribution(df)
    
    return stats, anomalies, correlation_matrix, daily_comparison, sales_dist
