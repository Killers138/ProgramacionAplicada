class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

    def percentage(self, part, whole):
        if whole == 0:
            raise ValueError("No se puede calcular el porcentaje con total cero")
        return (part / whole) * 100

