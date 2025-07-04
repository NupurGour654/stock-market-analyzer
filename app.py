# Entry point for Stock Market Analyzer

from stock_utils import fetch_stock_data, plot_closing_price

def main():
    symbol = input("Enter stock ticker symbol (e.g., AAPL): ").upper()
    data = fetch_stock_data(symbol)
    if data is not None:
        plot_closing_price(data, symbol)

if __name__ == "__main__":
    main()
