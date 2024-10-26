import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Create input fields for numbers
        tk.Label(self.root, text="Number 1:").grid(row=0, column=0)
        self.num1_entry = tk.Entry(self.root, width=18)
        self.num1_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Number 2:").grid(row=1, column=0)
        self.num2_entry = tk.Entry(self.root, width=18)
        self.num2_entry.grid(row=1, column=1)

        # Create operation buttons
        tk.Button(self.root, text="+", width=5, command=lambda: self.calculate("+")).grid(row=2, column=0)
        tk.Button(self.root, text="-", width=5, command=lambda: self.calculate("-")).grid(row=2, column=1)
        tk.Button(self.root, text="*", width=5, command=lambda: self.calculate("*")).grid(row=3, column=0)
        tk.Button(self.root, text="/", width=5, command=lambda: self.calculate("/")).grid(row=3, column=1)
        # Create calculate button
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_result)
        self.calculate_button.grid(row=4, column=0, columnspan=2)

        # Create result label
        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.grid(row=5, column=0, columnspan=2)

    def calculate(self, operation):
        try:
            self.num1 = float(self.num1_entry.get())
            self.num2 = float(self.num2_entry.get())
            self.operation = operation
        except ValueError:
            self.result_label['text'] = "Error: Invalid input!"

    def calculate_result(self):
        try:
            if self.operation == '+':
                result = self.num1 + self.num2
            elif self.operation == '-':
                result = self.num1 - self.num2
            elif self.operation == '*':
                result = self.num1 * self.num2
            elif self.operation == '/':
                if self.num2 != 0:
                    result = self.num1 / self.num2
                else:
                    self.result_label['text'] = "Error: Cannot divide by zero!"
                    return
            self.result_label['text'] = f"Result: {self.num1} {self.operation} {self.num2} = {result}"
        except AttributeError:
            self.result_label['text'] = "Error: Please select an operation!"

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()