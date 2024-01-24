# Sales Analysis Project

This project is dedicated to analyzing sales behavior at point-of-sale (POS) systems, focusing on daily sales trends and identifying anomalies.

## Project Structure

# Technologies Used
- Python
- Pandas
- Matplotlib

## Installation
Clone the repository and install the dependencies:

pip install -r requirements.txt

## Execution

To start the server:

- python main.py

The project is organized into several Python scripts, each handling a different aspect of the data analysis process:

- `analysis.py`: Contains functions for specific analyses, such as calculating statistics, identifying anomalies, and generating correlation matrices.
- `data_loading.py`: Includes functions to load and prepare the sales data.
- `data_processing.py`: Processes the data by invoking functions from `analysis.py`.
- `database_operations.py`: Manages database connections and SQL queries for data comparison.
- `main_analysis.py`: The main script that runs the data analysis using the above modules.
- `main_visualization.py`: Contains functions to visualize the analyzed data.
- `visualization.py`: Provides various plotting functions to showcase the sales data and analysis results.
- `main.py`: The entry point of the program that orchestrates the analysis and visualization process.

## Usage

To run the analysis:

1. Ensure you have Python and the necessary libraries installed.
2. Place your sales data files `checkout_1.csv` and `checkout_2.csv` in the project directory.
3. Run the `main.py` script to start the analysis and visualization process.


## Presentation Link:

https://drive.google.com/file/d/1xtN84ttQ_dIdTAfrs7KikVgp-4ykegwz/view?usp=drive_link
