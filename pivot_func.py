def pivot_sales_by_date_and_purchase_type(data):
    pivot = data.pivot_table(
        values='Price',
        index='Date of Purchase',
        columns='Purchase Type',
        aggfunc='sum',
        fill_value=0
    )
    return pivot


def pivot_avg_price_by_stations(data):
    pivot = data.pivot_table(
        values='Price',
        index='Departure Station',
        columns='Arrival Destination',
        aggfunc='mean',
        fill_value=0
    )
    return pivot


def pivot_delay_analysis(data):
    pivot = data.pivot_table(
        values='Transaction ID',
        index='Journey Status',
        columns='Reason for Delay',
        aggfunc='count',
        fill_value=0
    )
    return pivot


def pivot_total_purchase_type(data):
    pivot = data.pivot_table(
        values='Transaction ID',
        index='Purchase Type',
        aggfunc='count',
        fill_value=0
    )
    return pivot
