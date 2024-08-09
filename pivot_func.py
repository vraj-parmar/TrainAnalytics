# Function to create a pivot table for sales by date and purchase type
def pivot_sales_by_date_and_purchase_type(data):
    # Create a pivot table with 'Date of Purchase' as rows and 'Purchase Type' as columns
    # Values are the 'Price', aggregated by summing up the prices
    # Fill missing values with 0
    pivot = data.pivot_table(
        values='Price',
        index='Date of Purchase',
        columns='Purchase Type',
        aggfunc='sum',
        fill_value=0
    )
    return pivot

# Function to create a pivot table for average ticket price by departure and arrival stations
def pivot_avg_price_by_stations(data):
    # Create a pivot table with 'Departure Station' as rows and 'Arrival Destination' as columns
    # Values are the 'Price', aggregated by calculating the mean price
    # Fill missing values with 0
    pivot = data.pivot_table(
        values='Price',
        index='Departure Station',
        columns='Arrival Destination',
        aggfunc='mean',
        fill_value=0
    )
    return pivot

# Function to create a pivot table for delay analysis
def pivot_delay_analysis(data):
    # Create a pivot table with 'Journey Status' as rows and 'Reason for Delay' as columns
    # Values are the 'Transaction ID', aggregated by counting the occurrences
    # Fill missing values with 0
    pivot = data.pivot_table(
        values='Transaction ID',
        index='Journey Status',
        columns='Reason for Delay',
        aggfunc='count',
        fill_value=0
    )
    return pivot

# Function to create a pivot table for total number of purchases by type
def pivot_total_purchase_type(data):
    # Create a pivot table with 'Purchase Type' as rows
    # Values are the 'Transaction ID', aggregated by counting the occurrences
    # Fill missing values with 0
    pivot = data.pivot_table(
        values='Transaction ID',
        index='Purchase Type',
        aggfunc='count',
        fill_value=0
    )
    return pivot
