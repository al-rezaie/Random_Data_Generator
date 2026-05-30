import random
from string import digits

class Phone:
    constants = ["0917", "0936", "0938", "0939"]
    numbers = [str(x) for x in digits]
    
    def __init__(self, n_data):
        self.n_data = n_data
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            phone_number = random.choice(Phone.constants)
            for j in range(7):
                phone_number + random.choice(Phone.numbers)
            data.append(phone_number)
            
        return data