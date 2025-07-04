# Stock Market Analyzer

This is a simple Python project to analyze and visualize stock closing prices using data from Yahoo Finance.

## Features

- Fetches last 1-month historical data of a given stock.
- Visualizes the stock's closing price using a line chart.
- Uses `yfinance` for data and `matplotlib` for plotting.

## Technologies Used

- Python
- yfinance
- matplotlib
## Setup Instructions

1. Clone the repository
2. Install dependencies:pip install -r requirements.txt
3. Run the script: 
4. When prompted, enter the stock ticker symbol (for example: AAPL, INFY.NS, TCS.NS)
   
## Example Output

After running the app and entering a valid stock symbol like `AAPL`, a line chart of the stock’s closing prices over the past month will be displayed.


## Project Structure
stock-market-analyser/
1. app.py
2. stock_utils.py
3. requirements.txt
4. readme.md

## Data Source

All stock data is fetched using the Yahoo Finance API via the `yfinance` Python package.

## Author

Developed by Nupur Singh








