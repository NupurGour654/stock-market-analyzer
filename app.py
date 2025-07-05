# Entry point for Stock Market Analyzer

from stock_utils import fetch_stock_data, plot_closing_price, save_data_to_csv

def main():
    symbol = input("Enter stock ticker symbol (e.g., AAPL): ").strip().upper()
    print(f"Fetching data for {symbol}...")
    #data = fetch_stock_data(symbol)
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    data = fetch_stock_data(symbol, start, end)


    if data is not None:
        plot_closing_price(data, symbol)
        save_data_to_csv(data, symbol)
    else:
        print("Failed to fetch data. Please check the symbol and try again.")

if __name__ == "__main__":
    main()
