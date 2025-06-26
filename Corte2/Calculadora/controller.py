from model import Calculator
from view import CalculatorView
from tkinter import messagebox

class CalculatorController:
    def __init__(self):
        self.model = Calculator()
        self.view = CalculatorView(self)
        self.view.mainloop()

    def handle_add(self):
        a, b = self.view.get_input_values()
        if a is not None:
            result = self.model.add(a, b)
            self.view.show_result(result)

    def handle_subtract(self):
        a, b = self.view.get_input_values()
        if a is not None:
            result = self.model.subtract(a, b)
            self.view.show_result(result)

    def handle_multiply(self):
        a, b = self.view.get_input_values()
        if a is not None:
            result = self.model.multiply(a, b)
            self.view.show_result(result)

    def handle_divide(self):
        a, b = self.view.get_input_values()
        if a is not None:
            try:
                result = self.model.divide(a, b)
                self.view.show_result(result)
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def handle_percentage(self):
        part, whole = self.view.get_input_values()
        if part is not None:
            try:
                result = self.model.percentage(part, whole)
                self.view.show_result(f"{result:.2f}%")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

