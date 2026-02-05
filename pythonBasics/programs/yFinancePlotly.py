import yfinance as yf
import plotly.graph_objs as go
import plotly.io as pio
import time

pio.renderers.default = "browser"

ticker = "TSLA"
userTicker = input("Enter Ticker: ")

if userTicker:
    ticker = userTicker.upper()

data = yf.download(ticker, period="6mo", interval="1d", rounding=True)
data.columns = data.columns.droplevel(1)

print("Data from server for ticker:", ticker)
print(data)

chart = go.Figure()
chart.add_trace(go.Candlestick(
    x = data.index,
    open = data["Open"],
    high = data["High"],
    low = data["Low"],
    close = data["Close"],
    name = "Price chart"
))

chart.update_layout(
    title = ticker + " share price",
    yaxis_title = "Stock price (USD)",
)

chart.show()