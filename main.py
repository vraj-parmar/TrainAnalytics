# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pivot_func import *  # Import custom functions for data pivoting


# Function to load and preprocess data
def get_data(filepath):
    # Read CSV file into a DataFrame
    data = pd.read_csv(filepath)

    # Convert 'Date of Purchase' and 'Date of Journey' to datetime objects
    data['Date of Purchase'] = pd.to_datetime(data['Date of Purchase'], format='%d/%m/%Y')
    data['Date of Journey'] = pd.to_datetime(data['Date of Journey'], format='%d/%m/%Y')

    return data


# Function to calculate percentage change
def calculate_percentage_change(new, old):
    # Return percentage change, handle division by zero
    return ((new - old) / old) * 100 if old != 0 else float('inf')


# Main script execution
if __name__ == '__main__':
    # Load data from CSV file
    data = get_data('data/railway.csv')

    # Determine the latest and previous months
    latest_month = data['Date of Purchase'].max().month
    latest_year = data['Date of Purchase'].max().year
    previous_month = (latest_month - 1) if latest_month > 1 else 12
    previous_year = latest_year if latest_month > 1 else latest_year - 1

    # Filter data for the latest and previous months
    data_latest_month = data[
        (data['Date of Purchase'].dt.month == latest_month) & (data['Date of Purchase'].dt.year == latest_year)]
    data_previous_month = data[
        (data['Date of Purchase'].dt.month == previous_month) & (data['Date of Purchase'].dt.year == previous_year)]

    # Create pivot tables for the latest month
    pivot_sales_latest = pivot_sales_by_date_and_purchase_type(data_latest_month)
    pivot_total_purchases_latest = pivot_total_purchase_type(data_latest_month)
    pivot_delay_latest = pivot_delay_analysis(data_latest_month)

    # Calculate key metrics for the latest month
    total_sales_latest = pivot_sales_latest.sum().sum()  # Total sales amount
    avg_ticket_price_latest = data_latest_month['Price'].mean()  # Average ticket price
    total_delays_latest = pivot_delay_latest.sum().sum()  # Total delays in minutes
    total_online_purchases_latest = pivot_total_purchases_latest.loc[
        'Online', 'Transaction ID']  # Total online purchases
    total_station_purchases_latest = pivot_total_purchases_latest.loc[
        'Station', 'Transaction ID']  # Total station purchases

    # Create pivot tables for the previous month
    pivot_sales_previous = pivot_sales_by_date_and_purchase_type(data_previous_month)
    pivot_total_purchases_previous = pivot_total_purchase_type(data_previous_month)
    pivot_delay_previous = pivot_delay_analysis(data_previous_month)

    # Calculate key metrics for the previous month
    total_sales_previous = pivot_sales_previous.sum().sum()
    avg_ticket_price_previous = data_previous_month['Price'].mean()
    total_delays_previous = pivot_delay_previous.sum().sum()
    total_online_purchases_previous = pivot_total_purchases_previous.loc['Online', 'Transaction ID']
    total_station_purchases_previous = pivot_total_purchases_previous.loc['Station', 'Transaction ID']

    # Calculate percentage changes
    total_sales_change = calculate_percentage_change(total_sales_latest, total_sales_previous)
    avg_ticket_price_change = calculate_percentage_change(avg_ticket_price_latest, avg_ticket_price_previous)
    total_delays_change = calculate_percentage_change(total_delays_latest, total_delays_previous)
    online_purchases_change = calculate_percentage_change(total_online_purchases_latest,
                                                          total_online_purchases_previous)
    station_purchases_change = calculate_percentage_change(total_station_purchases_latest,
                                                           total_station_purchases_previous)

    # Set up the Streamlit page configuration
    st.set_page_config(layout="wide")
    st.title("Railway Analysis Dashboard")

    # Display the overview header
    st.header("Railway Data Overview")

    # Create columns to display metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Sales", f"£{total_sales_latest:,.2f}", f"{total_sales_change:.2f}%")
    col2.metric("Average Ticket Price", f"£{avg_ticket_price_latest:.2f}", f"{avg_ticket_price_change:.2f}%")
    col3.metric("Total Delays", f"{total_delays_latest} mins", f"{total_delays_change:.2f}%")
    col4.metric("Online Purchases", total_online_purchases_latest, f"{online_purchases_change:.2f}%")
    col5.metric("Station Purchases", total_station_purchases_latest, f"{station_purchases_change:.2f}%")

    # Create columns for displaying charts
    col1, col2 = st.columns(2)

    # Display the total sales by date and purchase type chart
    with col1:
        st.subheader("Total Sales by Date and Purchase Type")
        sales_fig = px.line(pivot_sales_latest, title='Total Sales by Date and Purchase Type')
        st.plotly_chart(sales_fig, use_container_width=True)

        # Display the total number of online and station purchase types chart
        st.subheader("Total Number of Online and Station Purchase Types")
        purchase_fig = px.pie(pivot_total_purchases_latest, names=pivot_total_purchases_latest.index,
                              values='Transaction ID', title='Total Number of Online and Station Purchase Types')
        st.plotly_chart(purchase_fig, use_container_width=True)

    # Display the average ticket price and delay analysis charts
    with col2:
        st.subheader("Average Ticket Price by Departure and Arrival Stations")
        avg_price_fig = px.bar(pivot_avg_price_by_stations(data_latest_month),
                               title='Average Ticket Price by Departure and Arrival Stations')
        st.plotly_chart(avg_price_fig, use_container_width=True)

        st.subheader("Delay Analysis by Journey Status and Reason for Delay")
        delay_fig = go.Figure(data=[
            go.Bar(name=col, x=pivot_delay_latest.index, y=pivot_delay_latest[col]) for col in
            pivot_delay_latest.columns
        ])
        delay_fig.update_layout(barmode='stack', title='Delay Analysis by Journey Status and Reason for Delay')
        st.plotly_chart(delay_fig, use_container_width=True)
