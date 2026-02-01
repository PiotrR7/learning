import tkinter as tk

window = tk.Tk()

btn1 = tk.Button(
    window,
    text = "Button 1",
    bg = "red",
)
btn1.grid(row = 0, column = 0, ipadx = 5, ipady = 5)

btn2 = tk.Button(
    window,
    text = "Button 2",
    bg = "blue",
)
btn2.grid(row = 0, column = 1, ipadx = 5, ipady = 5)

btn3 = tk.Button(
    window,
    text = "Button 3",
    bg = "green",
)
btn3.grid(row = 0, column = 2, ipadx = 5, ipady = 5)

btn4 = tk.Button(
    window,
    text = "Button 4",
    bg = "yellow",
)
btn4.grid(row = 1, column = 0, ipadx = 5, ipady = 5)

btn5 = tk.Button(
    window,
    text = "Button 5",
    bg = "purple",
)
btn5.grid(row = 1, column = 1, ipadx = 5, ipady = 5)

btn6 = tk.Button(
    window,
    text = "Button 6",
    bg = "black",
)
btn6.grid(row = 1, column = 2, ipadx = 5, ipady = 5)

btn7 = tk.Button(
    window,
    text = "Button 7",
    bg = "silver",
)
btn7.grid(row = 2, column = 0, ipadx = 5, ipady = 5, columnspan = 3, sticky = "ew")


window.mainloop()