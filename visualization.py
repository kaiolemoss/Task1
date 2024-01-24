import matplotlib.pyplot as plt

def plot_differences(df):
    plt.figure(figsize=(15, 6))
    plt.plot(df['time'], df['diff_yesterday'], label='Yesterday')
    plt.plot(df['time'], df['diff_same_day_last_week'], label='Same Day Last Week')
    plt.plot(df['time'], df['diff_avg_last_week'], label='Avg Last Week')
    plt.plot(df['time'], df['diff_avg_last_month'], label='Avg Last Month')
    plt.xticks(rotation=45)
    plt.ylabel('Difference (%)')
    plt.title('Differences for Checkout')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_anomalies(df, anomalies, column='today'):
    """
    Plots the anomalies on a line chart.
    Args:
    df (DataFrame): DataFrame original containing all the data.
    anomalies (DataFrame): DataFrame containing the anomalies.
    column (str): Name of the column containing the data to be plotted.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['time'], df[column], label='Sales', color='blue')
    plt.scatter(anomalies['time'], anomalies[column], color='red', label='Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Sales')
    plt.title('Sales anomalies')
    plt.legend()
    plt.grid(True)
    plt.show()

    pass

def plot_trends(df, column='today'):
    plt.figure(figsize=(12, 6))
    plt.plot(df['time'], df[column], label='Sales Trend', color='green')
    plt.xlabel('Time')
    plt.ylabel('Sales')
    plt.title('Sales Trend Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_daily_comparison(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['time'], df['today'], label='Sales Today', color='blue')
    plt.plot(df['time'], df['avg_last_week'], label='Avg Last Week', color='orange')
    plt.plot(df['time'], df['avg_last_month'], label='Avg Last Month', color='purple')
    plt.xlabel('Tempo')
    plt.ylabel('Vendas')
    plt.title('Daily Sales Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_sales_distribution(df, column='today'):
    plt.figure(figsize=(10, 6))
    plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.title(f'Sales Distribution ({column})')
    plt.grid(True)
    plt.show()

def plot_percent_change(df, periods):
    plt.figure(figsize=(12, 6))
    for period in periods:
        plt.plot(df['time'], df[f'percent_change_{period}'], label=f'Change vs {period}')
    plt.xlabel('Time')
    plt.ylabel('Percent Change')
    plt.title('Daily Percent Change Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_moving_averages(df, column='today', window_size=7):
    plt.figure(figsize=(12, 6))
    plt.plot(df['time'], df[column], label='Original', alpha=0.5)
    plt.plot(df['time'], df[f'moving_avg_{window_size}'], label=f'Moving Avg ({window_size} days)', color='red')
    plt.xlabel('Time')
    plt.ylabel('Sales')
    plt.title('Moving Averages of Sales')
    plt.legend()
    plt.grid(True)
    plt.show()
