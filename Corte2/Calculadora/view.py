import tkinter as tk
from tkinter import messagebox

class CalculatorView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Calculadora MVC")
        self.geometry("300x300")
        self.configure(padx=10, pady=10)

        self.label1 = tk.Label(self, text="Número A:")
        self.label1.pack()
        self.entry1 = tk.Entry(self)
        self.entry1.pack()

        self.label2 = tk.Label(self, text="Número B:")
        self.label2.pack()
        self.entry2 = tk.Entry(self)
        self.entry2.pack()

        self.result_label = tk.Label(self, text="Resultado:")
        self.result_label.pack(pady=10)

        tk.Button(self, text="Sumar", command=self.controller.handle_add).pack(fill="x")
        tk.Button(self, text="Restar", command=self.controller.handle_subtract).pack(fill="x")
        tk.Button(self, text="Multiplicar", command=self.controller.handle_multiply).pack(fill="x")
        tk.Button(self, text="Dividir", command=self.controller.handle_divide).pack(fill="x")
        tk.Button(self, text="Porcentaje (A de B)", command=self.controller.handle_percentage).pack(fill="x")

    def get_input_values(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos.")
            return None, None

    def show_result(self, result):
        self.result_label.config(text=f"Resultado: {result}")

