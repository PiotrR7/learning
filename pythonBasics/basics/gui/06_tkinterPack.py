import tkinter as tk

window = tk.Tk()

label1 = tk.Label(
    window,
    text = "label 1",
    bg = "blue",
)
label1.pack(
    side = tk.TOP,
    expand = True,
    fill = tk.BOTH,
)

label2 = tk.Label(
    window,
    text = "label 2",
    bg = "red",
)
label2.pack(
    side = tk.BOTTOM,
    expand = True,
    fill = tk.BOTH,
)

btn1 = tk.Button(
    window,
    bg = "black",
    text = "btn1",
    fg = "white",
)
btn1.pack(
    side = tk.LEFT,
    expand = True,
    fill = tk.BOTH,
)

btn2 = tk.Button(
    window,
    bg = "yellow",
    text = "btn2",
)
btn2.pack(
    side = tk.RIGHT,
    expand = True,
    fill = tk.BOTH,
)

window.mainloop()