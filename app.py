# Entry point for Stock Market Analyzer

from stock_utils import fetch_stock_data, plot_closing_price, save_data_to_csv
from datetime import datetime
from stock_utils import fetch_stock_data, plot_closing_price, save_data_to_csv

def validate_date_format(date_str):
    """Check if date is in YYYY-MM-DD format"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def main():
   symbol = input("Enter stock ticker symbol (e.g., AAPL): ").strip().upper()
    if not symbol:
    print("Stock symbol cannot be empty.")
    return

print(f"Fetching data for {symbol}...")

    #data = fetch_stock_data(symbol)
start = input("Enter start date (YYYY-MM-DD): ")
end = input("Enter end date (YYYY-MM-DD): ")

if not (validate_date_format(start) and validate_date_format(end)):
    print("Invalid date format. Please use YYYY-MM-DD.")
    return

    data = fetch_stock_data(symbol, start, end)


    if data is not None:
        plot_closing_price(data, symbol)
        save_data_to_csv(data, symbol)
    else:
        print("Failed to fetch data. Please check the symbol and try again.")

if __name__ == "__main__":
    main()
