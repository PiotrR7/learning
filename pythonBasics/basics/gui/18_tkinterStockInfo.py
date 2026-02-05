import tkinter as tk
import yfinance as yf

window = tk.Tk()
window.title("Stock Info")

topWidget = tk.Frame(window)
label = tk.Label(
    topWidget,
    text = "Write stock ticker: "
)
label.pack(side = tk.LEFT)

entry = tk.Entry(
    topWidget,
)
entry.pack(side = tk.RIGHT)
topWidget.pack()

scrollbar = tk.Scrollbar(window)
textBox = tk.Text(
    window,
    height = 10,
    width = 70,
    padx = 5,
    pady = 5,
    font = "Helvetica 12",
)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
textBox.pack(expand = True, fill = "both")
scrollbar.config(command = textBox.yview)
textBox.config(yscrollcommand = scrollbar.set)

def downloadData(event):
    textBox.delete(1.0, tk.END)
    stock = str(event.widget.get())

    if stock:
        print("downloading data:", stock)
    else:
        return

    stock = stock.upper()

    stockData = yf.Ticker(stock)
    textBox.insert(tk.END, "Ticker: " + str(stock) + "\n\n")

    for key in stockData.info.keys():
        try:
            value = str(key) + ": " + stockData.info[str(key)] + "\n"
            textBox.insert(tk.END, value)
        except:
            pass

    history = stockData.history(period = "1mo", interval = "1d")
    textBox.insert(tk.END, history)


entry.bind("<Return>", downloadData)

window.mainloop()