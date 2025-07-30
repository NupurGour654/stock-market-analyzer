import yfinance as yf
import matplotlib.pyplot as plt

# Added fetch_stock_data function
def fetch_stock_data(symbol, start=None, end=None):
     """Fetch stock data using yfinance for a given symbol and date range."""
    try:
        data = yf.download(symbol, start=start, end=end)
        if data.empty:
            print("No data found.")
            return None
        return data
    except Exception as e:
        print("Error fetching stock data:", e)
        return None

# Added plot_closing_price function
def plot_closing_price(data, symbol):
     """Plot and save the closing price line graph for a stock."""
    #data['Close'].plot(title=f"{symbol} Closing Price (Last 1 Month)")
     start = data.index.min().strftime("%Y-%m-%d")
     end = data.index.max().strftime("%Y-%m-%d")
     data['Close'].plot(title=f"{symbol} Closing Price ({start} to {end})")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.grid(True)
    plt.savefig(f"{symbol}_closing_price.png")
    plt.show()
    
def save_data_to_csv(data, symbol):
     """Save stock data to a CSV file named after the stock symbol."""
    filename = f"{symbol.lower()}_data.csv"
    data.to_csv(filename)
    print(f"Data saved to {filename}")

