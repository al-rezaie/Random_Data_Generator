import random

class IPv4:
    def __init__(self, n_data):
        self.n_data = n_data
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            ip = ""
            for i in range(4):
                ip + str(random.randint(0, 255))
            data.append(ip)
            
        return data