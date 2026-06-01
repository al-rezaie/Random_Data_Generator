import random
import datetime

date_format = "%d-%m-%Y"

class Date:
    def __init__(self, values):
        self.start_date = values[0]
        self.end_date = values[1]
        self.n_data = values[2]
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            date = self.start_date + datetime.timedelta(days=random.randint(0, (self.end_date - self.start_date).days))
            data.append(date.date())
            
        return data
    
    @classmethod
    def get_fields(*args):
        string_start_date = input("Enter the start date: ")
        start_date = datetime.datetime.strptime(string_start_date, date_format)
        
        string_end_date = input("Enter the end date: ")
        end_date = datetime.datetime.strptime(string_end_date, date_format)
        
        n_data = int(input("Enter the number of data you want to generate: "))
        
        return [start_date, end_date, n_data]