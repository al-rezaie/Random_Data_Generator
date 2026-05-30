import random
import datetime

class Date:
    def __init__(self, start_date, end_date, n_data):
        self.start_date = datetime.date(start_date)
        self.end_date = datetime.date(end_date)
        self.n_data = n_data
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            date = self.start_date + datetime.timedelta(days=random.randint(0, (self.end_date - self.start_date).days()))
            data.append(date)
            
        return data