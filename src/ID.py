from uuid import uuid4

class ID:
    def __init__(self, n_data):
        self.n_data = n_data
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            Id = uuid4()
            data.append(Id)
            
        return data