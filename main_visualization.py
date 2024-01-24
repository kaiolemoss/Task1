from visualization import (
    plot_differences, plot_anomalies, plot_trends, plot_daily_comparison,
    plot_sales_distribution, plot_moving_averages, plot_percent_change
)

def run_visualizations(df1, df2, anomalies1, anomalies2):
    plot_differences(df1)
    #plot_anomalies(df1, anomalies1)
    plot_trends(df1)
    plot_daily_comparison(df1)
    plot_sales_distribution(df1)
    plot_percent_change(df1, ['yesterday', 'same_day_last_week', 'avg_last_week', 'avg_last_month'])
    plot_moving_averages(df1)

    plot_differences(df2)
    #plot_anomalies(df2, anomalies2)
    plot_trends(df2)
    plot_daily_comparison(df2)
    plot_sales_distribution(df2)
    plot_percent_change(df2, ['yesterday', 'same_day_last_week', 'avg_last_week', 'avg_last_month'])
    plot_moving_averages(df2)
