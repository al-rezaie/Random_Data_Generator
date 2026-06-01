import random
import datetime

class Time:
    def __init__(self, n_data):
        self.n_data = n_data
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            time = datetime.time(hour=random.randint(0, 23), minute=random.randint(0, 59), second=random.randint(0,59))
            data.append(time)
        
        return data
    
    def get_fields(*args):
        n_data = int(input("Enter the number of data you want to generate: "))
        
        return n_data