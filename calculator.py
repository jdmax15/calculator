


class Calculator:
    def __init__(self, history_limit):
        self.history = []
        self.history_limit = history_limit
        self.operations = ['add', 'subtract', 'multiply', 'divide']

    def add(self, x, y):
        answer = x + y
        self.history.append(f"{x} + {y} = {answer}")
        return answer
    
    def subtract(self, x, y):
        answer = x - y
        self.history.append(f"{x} - {y} = {answer}")
        return answer
    
    def multiply(self, x, y):
        answer = x * y
        self.history.append(f"{x} * {y} = {answer}")
        return answer
    
    def divide(self, x, y):
        answer = x / y
        self.history.append(f"{x} / {y} = {answer}")
        return answer
    
    def get_history(self):
        for line in self.history:
            print(line)
    

calc = Calculator(10)

print(calc.add(2, 3))
print(calc.subtract(3, 2))
print(calc.multiply(2, 3))
print(int(calc.divide(4, 2)))
calc.get_history()
#print(calc.history_limit)