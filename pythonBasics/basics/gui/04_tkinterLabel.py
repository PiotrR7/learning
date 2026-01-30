import tkinter as tk
import os

window = tk.Tk()
window.title("Application")

logo = tk.PhotoImage(file = "image.png")

label1 = tk.Label(
    window,
    text = "Hello World!",
    foreground = "white",
    background = "black",
    width = 50,
    height = 5,
    cursor = "dot",
    font = "Calibri 20 bold",
    anchor = tk.CENTER,
    padx = 10,
    pady = 5,
)
label1.pack()

label2 = tk.Label(
    window,
    text = "Hello again!",
)
label2.pack()

label3 = tk.Label(
    text = "Hello World!",
    image = logo,
    compound = tk.CENTER,
    foreground = "red",
    width = 500,
    height = 500,
)
label3.pack()
label3.configure(text = "Hello World!\nAGAIN!!")

window.mainloop()