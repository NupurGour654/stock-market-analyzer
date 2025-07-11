import yfinance as yf
import matplotlib.pyplot as plt

# Added fetch_stock_data function
def fetch_stock_data(symbol, start=None, end=None):
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
    data['Close'].plot(title=f"{symbol} Closing Price (Last 1 Month)")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.grid(True)
    plt.savefig(f"{symbol}_closing_price.png")
    plt.show()
    
def save_data_to_csv(data, symbol):
    filename = f"{symbol}_data.csv"
    data.to_csv(filename)
    print(f"Data saved to {filename}")

