import pandas as pd
import numpy as np

def calculate_statistics(df):
    return df.describe()

def calculate_differences(df):
    for column in ['yesterday', 'same_day_last_week', 'avg_last_week', 'avg_last_month']:
        df[f'diff_{column}'] = ((df['today'] - df[column]) / df[column]).replace([np.inf, -np.inf], np.nan).fillna(0) * 100
    return df

def identify_anomalies(df, column='today', threshold=1.5):
    """
    Identifies days with abnormally high or low sales.
    
    Args:
    df (DataFrame): DataFrame containing data.
    column (str):   Name of the column to analyze for anomalies.
    threshold (float): Threshold for considering a sale as anomalous, based on standard deviation.

    Returns:
    DataFrame: DataFrame containing anomalies.
    """
    mean_value = df[column].mean()
    std_dev = df[column].std()
    anomalies = df[np.abs(df[column] - mean_value) > threshold * std_dev]
    return anomalies


def run_sql_comparison(conn):
    sql_query = """
    SELECT 
        c1.time, 
        c1.today AS today_checkout1, 
        c2.today AS today_checkout2
    FROM 
        checkout1 c1
    JOIN 
        checkout2 c2 ON c1.time = c2.time
    """

    # Executing the SQL query
    comparison_df = pd.read_sql_query(sql_query, conn)

    return comparison_df

def calculate_correlation(df):
    # Exclude non-numeric columns before calculating correlation
    numeric_df = df.select_dtypes(include=[np.number])
    return numeric_df.corr()

def daily_percentage_comparison(df):
    df['percent_change_last_week'] = (df['today'] - df['avg_last_week']) / df['avg_last_week'] * 100
    df['percent_change_last_month'] = (df['today'] - df['avg_last_month']) / df['avg_last_month'] * 100
    return df[['time', 'percent_change_last_week', 'percent_change_last_month']]

def sales_distribution(df, column='today'):
    return df[column].describe()

def calculate_daily_percent_change(df):
    for period in ['yesterday', 'same_day_last_week', 'avg_last_week', 'avg_last_month']:
        if period in df.columns:
            df[f'percent_change_{period}'] = (df['today'] - df[period]) / df[period] * 100
        else:
            print(f"Aviso: A coluna '{period}' não existe no DataFrame.")
    return df

def calculate_moving_averages(df, column='today', window_size=7):
    df[f'moving_avg_{window_size}'] = df[column].rolling(window=window_size).mean()
    return df

