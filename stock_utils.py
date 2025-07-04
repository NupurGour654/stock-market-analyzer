import yfinance as yf
import matplotlib.pyplot as plt

# Added fetch_stock_data function
def fetch_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1mo")
        return hist
    except Exception as e:
        print("Error fetching data:", e)
        return None

def plot_closing_price(data, symbol):
    data['Close'].plot(title=f"{symbol} Closing Price (Last 1 Month)")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.grid(True)
    plt.savefig(f"{symbol}_closing_price.png")
    plt.show()
