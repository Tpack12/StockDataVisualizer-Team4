from stock_api import fetch_stock_data
from chart_generator import generate_chart
from utils import validate_date_range

def show_menu(title, options):
    while True:
        print(f"\n{title}")
        print("-" * len(title))
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        try:
            choice = int(input(f"\nEnter your choice (1 - {len(options)}): "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print(" Invalid choice. Please select a valid option.")
        except ValueError:
            print(" Please enter a number.")

def main():
    print("Stock Data Visualizer")
    print("=" * 25)

    while True:
        symbol = input("\nEnter the stock symbol you are looking for: ").upper()

        chart_choice = show_menu("Chart Types", ["Bar", "Line"])
        chart_type = "bar" if chart_choice == 1 else "line"

        time_series_choice = show_menu(
            "Select the Time Series of the chart you want to Generate",
            ["Intraday", "Daily", "Weekly", "Monthly"]
        )

        time_series_map = {1: "INTRADAY", 2: "DAILY", 3: "WEEKLY", 4: "MONTHLY"}
        time_series = time_series_map.get(time_series_choice, "DAILY")

        start_date = input("Enter the start Date (YYYY-MM-DD): ")
        end_date = input("Enter the end Date (YYYY-MM-DD): ")

        if not validate_date_range(start_date, end_date):
            print(" Invalid date range. Please try again.")
            continue

        data = fetch_stock_data(symbol, time_series)
        if data:
            generate_chart(data, chart_type, start_date, end_date, symbol)
        else:
            print(" Failed to retrieve stock data.")

        more = input("\nWould you like to view more stock data? Press 'y' to continue: ").lower()
        if more != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

