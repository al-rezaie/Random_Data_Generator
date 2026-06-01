import random

class IPv4:
    def __init__(self, n_data):
        self.n_data = n_data
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            ip = ""
            for i in range(4):
                ip += str(random.randint(0, 255))
                if i != 3:
                    ip += "."
            data.append(ip)
            
        return data
    
    def get_fields(*args):
        n_data = int(input("Enter the number of data you want to generate: "))
        
        return n_data