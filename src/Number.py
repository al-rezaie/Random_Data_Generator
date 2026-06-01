import random

class Continuous:
    def __init__(self, values):
        self.range_start = values[0]
        self.range_end = values[1]
        self.n_decimal = values[2]
        self.n_data = values[3]
        
    def create_list(self):
        numbers_list = []
        for i in range(self.n_data):
            number = round(random.uniform(self.range_start, self.range_end), self.n_decimal)
            numbers_list.append(number)
        return numbers_list
    
    @classmethod
    def get_fields(*args):
        range_start = float(input("Enter the start of the range: "))
        range_end = float(input("Enter the end of the range: "))
        n_decimal = int(input("Enter the number of decimals after '.': "))
        n_data = int(input("Enter the number of data you want to generate: "))
        
        return [range_start, range_end, n_decimal, n_data]
    
class Discrete:
    def __init__(self, values):
        self.range_start = values[0]
        self.range_end = values[1]
        self.n_data = values[2]
        
    def create_list(self):
        numbers_list = []
        for i in range(self.n_data):
            number = random.randint(self.range_start, self.range_end)
            numbers_list.append(number)
        return numbers_list
    
    @classmethod
    def get_fields(*args):
        range_start = int(input("Enter the start of the range: "))
        range_end = int(input("Enter the end of the range: "))
        n_data = int(input("Enter the number of data you want to generate: "))
        
        return [range_start, range_end, n_data]