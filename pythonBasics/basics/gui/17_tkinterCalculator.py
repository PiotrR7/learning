import tkinter as tk

window = tk.Tk()
window.title("Calculator")

class Calculator:
    def __init__(self, window):
        self.window = window
        self.equationStrVar = tk.StringVar()
        self.expressionStr = ""
        self.calcKeyboard = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", "Clear", "=", "/"]
        ]
        self.prepareGui(window)

    def prepareGui(self, window):
        window.geometry("260x130")
        self.expressionField = tk.Entry(window, textvariable = self.equationStrVar)
        self.expressionField.grid(columnspan = 4, ipadx = 60)

        rowIndex = 0
        while rowIndex < len(self.calcKeyboard):
            calcRow = self.calcKeyboard[rowIndex]

            columnIndex = 0
            while columnIndex < len(calcRow):
                buttonText = calcRow[columnIndex]
                button = tk.Button(
                    window,
                    text = buttonText,
                    height = 1,
                    width = 8,
                    command = lambda v = buttonText: self.buttonPressed(v)
                )
                button.grid(column = columnIndex, row = rowIndex + 1)
                columnIndex += 1
            rowIndex += 1

    def buttonPressed(self, value):
        print("Button Pressed", value)

        if value == "Clear":
            self.expressionStr = ""
            self.equationStrVar.set("")
            return

        if value == "=":
            result = str(eval(self.expressionStr))
            self.expressionStr = ""
            self.equationStrVar.set(result)
            return

        self.expressionStr += value
        self.equationStrVar.set(self.expressionStr)

calc = Calculator(window)

window.mainloop()