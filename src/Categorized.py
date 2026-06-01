import random

class Categorized:
    def __init__(self, values):
        self.categories_list = values[0]
        self.n_data = values[1]
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            data.append(random.choice(self.categories_list))
            
        return data
    
    @classmethod
    def get_fields(*args):
        categories_list = input("Enter categories list seperated with ,: ").strip().split(",")
        n_data = int(input("Enter the number of data you want to generate: "))
        
        values = [categories_list, n_data]
        return values