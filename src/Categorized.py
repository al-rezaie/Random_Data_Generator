import random

class Categorized():
    def __init__(self, categories_list, n_data):
        self.categories_list = categories_list
        self.n_data = n_data
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            data.append(random.choice(self.categories_list))
            
        return data