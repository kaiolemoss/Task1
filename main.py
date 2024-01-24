from main_analysis import run_analysis
from main_visualization import run_visualizations

checkout1_path = 'checkout_1.csv'
checkout2_path = 'checkout_2.csv'

checkout1_df, checkout2_df, stats1, anomalies1, correlation_matrix1, daily_comparison1, sales_dist1, \
stats2, anomalies2, correlation_matrix2, daily_comparison2, sales_dist2 = run_analysis(checkout1_path, checkout2_path)

run_visualizations(checkout1_df, checkout2_df, anomalies1, anomalies2)
