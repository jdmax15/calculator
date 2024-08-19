


class Calculator:
    def __init__(self, history_limit):
        self.history = []
        self.history_limit = history_limit
        self.operations = ['add', 'subtract', 'multiply', 'divide']

    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y
    
    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        return x / y
    

calc = Calculator

result = calc.add(2, 3)

print(result)