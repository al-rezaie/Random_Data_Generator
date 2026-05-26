import random

class Continuous:
    def __init__(self, range_start, range_end, n_decimal, n_data):
        self.range_start = range_start
        self.range_end = range_end
        self.n_decimal = n_decimal
        self.n_data = n_data
        
    def create_list(self):
        numbers_list = []
        for i in range(self.n_data):
            number = round(random.uniform(self.range_start, self.range_end), self.n_decimal)
            numbers_list.append(number)
        return numbers_list
    
class Discrete:
    def __init__(self, range_start, range_end, n_data):
        self.range_start = range_start
        self.range_end = range_end
        self.n_data = n_data
        
    def create_list(self):
        numbers_list = []
        for i in range(self.n_data):
            number = random.randint(self.range_start, self.range_end)
            numbers_list.append(number)
        return numbers_list