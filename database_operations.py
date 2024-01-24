import sqlite3
import pandas as pd

def create_db_connection():
    #Creates and returns an in-memory database connection.
    return sqlite3.connect(':memory:')

def load_data_to_sql(df, table_name, conn):
    #Loads a Pandas DataFrame into a SQL table.
    df.to_sql(table_name, conn, index=False)

def run_comparison_query(conn):
    #Executes the comparison SQL query and returns the result.
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
    return pd.read_sql_query(sql_query, conn)
