# TrainAnalytics


## Example Screenshots

![TrainAnalytics_Screenshot](https://github.com/user-attachments/assets/5ac5b20e-5cce-479d-8096-0117dd1cbbf3)

## Overview

`TrainAnalytics` is a Python and Streamlit project designed for data visualisation and analysis of railway data. It provides insights into various metrics related to railway sales, ticket prices, purchase types, and delays by visualising data from a CSV file. The project includes functionalities to compare metrics between the latest and previous months.

## Project Structure

The project consists of the following files:

- `data/railway.csv`: CSV file containing the railway data.
- `main.py`: Main script to load data, process it, and display interactive visualisations using Streamlit.
- `pivot_func.py`: Contains custom functions to create pivot tables for various analyses.

## Requirements

To run this project, you need to have the following Python packages installed:

- `pandas`
- `plotly`
- `streamlit`

You can install these packages using pip:

```bash
pip install pandas plotly streamlit
```

## Usage

1. **Setup**: Make sure you have the required libraries installed and the `railway.csv` file is located in the `data/` directory.

2. **Running the Application**: Execute the `main.py` script using Streamlit. In your terminal, navigate to the project directory and run:

    ```bash
    streamlit run main.py
    ```

3. **Viewing the Dashboard**: Once the application starts, open your web browser and go to the URL provided by Streamlit (typically `http://localhost:8501`).

## Functionality

### Data Loading and Preprocessing

- **`get_data(filepath)`**: Reads the CSV file and preprocesses the data by converting date columns to datetime objects.

### Metrics Calculation

- **`calculate_percentage_change(new, old)`**: Calculates the percentage change between two values.

### Pivot Functions

- **`pivot_sales_by_date_and_purchase_type(data)`**: Creates a pivot table for total sales by date and purchase type.
- **`pivot_avg_price_by_stations(data)`**: Creates a pivot table for average ticket price by departure and arrival stations.
- **`pivot_delay_analysis(data)`**: Creates a pivot table for delay analysis by journey status and reason for delay.
- **`pivot_total_purchase_type(data)`**: Creates a pivot table for the total number of purchases by type.

### Streamlit Dashboard

- **Overview Metrics**: Displays key metrics such as total sales, average ticket price, total delays, online purchases, and station purchases with percentage changes compared to the previous month.
- **Charts**:
  - Total Sales by Date and Purchase Type (Line Chart)
  - Total Number of Online and Station Purchases (Pie Chart)
  - Average Ticket Price by Departure and Arrival Stations (Bar Chart)
  - Delay Analysis by Journey Status and Reason for Delay (Stacked Bar Chart)

## Files Description

- **`main.py`**: This script loads the data, performs calculations, and uses Streamlit to display the results and visualizations.
- **`pivot_func.py`**: Contains functions to create pivot tables for various analyses.
