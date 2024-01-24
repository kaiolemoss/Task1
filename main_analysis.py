from data_loading import load_data, prepare_data
from data_processing import process_data, analyze_data
import database_operations as db_ops

def run_analysis(checkout1_path, checkout2_path):
    checkout1_df = prepare_data(load_data(checkout1_path))
    checkout2_df = prepare_data(load_data(checkout2_path))

    checkout1_df = process_data(checkout1_df)
    checkout2_df = process_data(checkout2_df)

    conn = db_ops.create_db_connection()
    db_ops.load_data_to_sql(checkout1_df, 'checkout1', conn)
    db_ops.load_data_to_sql(checkout2_df, 'checkout2', conn)
    comparison_df = db_ops.run_comparison_query(conn)
    print(comparison_df.head())
    comparison_df.to_csv('comparison_data.csv', index=False)
    print("Comparison data saved in comparison_data.csv")



    stats1, anomalies1, correlation_matrix1, daily_comparison1, sales_dist1 = analyze_data(checkout1_df)
    print("Correlation Matrix for Checkout 1:\n", correlation_matrix1)
    correlation_matrix1.to_csv('correlation_matrix1.csv', index=False)
    print("Correlation Matrix for Checkout 1 saved in correlation_matrix1.csv")

    stats2, anomalies2, correlation_matrix2, daily_comparison2, sales_dist2 = analyze_data(checkout2_df)
    print("Correlation Matrix for Checkout 2:\n", correlation_matrix2)
    correlation_matrix2.to_csv('correlation_matrix2.csv', index=False)
    print("Correlation Matrix for Checkout 2 saved in correlation_matrix2.csv")


    print(daily_comparison1.head())
    daily_comparison1.to_csv('daily_comparison1.csv', index=False)
    print("Daily comparision for Checkout 1 saved in daily_comparison1.csv")
    print(sales_dist1)

    print(daily_comparison2.head())
    daily_comparison2.to_csv('daily_comparison2.csv', index=False)
    print("Daily comparision for Checkout 2 saved in daily_comparison2.csv")
    print(sales_dist2)


    stats2, anomalies2, correlation_matrix2, daily_comparison2, sales_dist2 = analyze_data(checkout2_df)

    return checkout1_df, checkout2_df, stats1, anomalies1, correlation_matrix1, daily_comparison1, sales_dist1, \
           stats2, anomalies2, correlation_matrix2, daily_comparison2, sales_dist2
