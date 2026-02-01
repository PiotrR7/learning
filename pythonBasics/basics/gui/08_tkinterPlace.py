import tkinter as tk

window = tk.Tk()

label1 = tk.Label(
    window,
    text = "Label 1",
    bg = "red",
)
label1.place(x = 0, y = 0, width = 50, height = 35)

label2 = tk.Label(
    window,
    text = "Label 2",
    bg = "green",
)
label2.place(x = 70, y = 70, width = 90, height = 35)

window.mainloop()