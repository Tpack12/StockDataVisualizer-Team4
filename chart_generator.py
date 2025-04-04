import matplotlib.pyplot as plt # type: ignore
from datetime import datetime

def generate_chart(data, chart_type, start_date, end_date, symbol):
    # Convert string dates to datetime objects
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")

    # Filter data based on date range
    filtered_data = {
        date: values for date, values in data.items()
        if start_dt <= datetime.strptime(date, "%Y-%m-%d") <= end_dt
    }

    if not filtered_data:
        print("No data available in the selected date range.")
        return

    # Sort dates
    sorted_dates = sorted(filtered_data.keys())
    closing_prices = [float(filtered_data[date]['4. close']) for date in sorted_dates]

    # Plot the chart
    plt.figure(figsize=(10, 5))
    if chart_type == "bar":
        plt.bar(sorted_dates, closing_prices, color='skyblue')
    else:
        plt.plot(sorted_dates, closing_prices, marker='o', linestyle='-', color='navy')

    plt.title(f"{symbol} Closing Prices ({start_date} to {end_date})")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()
