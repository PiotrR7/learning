import tkinter as tk

window = tk.Tk()

button = tk.Button(
    window,
    text = "Click me",
    bd = 10,
    fg = "red",
    bg = "green",
    activebackground = "blue",
    activeforeground = "silver",
    font = "Helvetica 20",
    height = 3,
    width = 20,
    padx = 10,
    pady = 10,
    relief = "groove",
    command = lambda: print("Button clicked")
)
button.pack()

window.mainloop()