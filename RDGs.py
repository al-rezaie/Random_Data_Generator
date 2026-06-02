import random
import datetime
import string
from string import digits
from uuid import uuid4

class Categorized:
    fields = {
        "categories_list": ["Enter categories list seperated with ,: ", "list"],
        "n_data": ["Enter the number of data you want to generate: ", "int"]
    }
    
    def __init__(self, values):
        self.categories_list = values[0]
        self.n_data = values[1]
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            data.append(random.choice(self.categories_list))
            
        return data
    
class Date:
    date_format = "%d-%m-%Y"
    fields = {
        "start_date": ["Enter the start date: ", "date"],
        "end_date": ["Enter the end date: ", "date"],
        "n_data": ["Enter the number of data you want to generate: ", "int"]
    }
    
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
    
class Email:
    characters = string.ascii_letters + string.digits
    prefixes = ["@gmail.com", "@yahoo.com", "@outlook.com"]
    fields = {
        "n_data": ["Enter the numbe of data you want to generate: ", "int"]
    }
    
    def __init__(self, values):
        self.n_data = values[0]
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            n_characters = random.randint(3, 11)
            email_characters = random.choices(Email.characters, k=n_characters)
            email = ""
            for c in email_characters:
                email += c
            email += random.choice(Email.prefixes)
            data.append(email)
            
        return data
    
class ID:
    fields = {
        "n_data": ["Enter the numbe of data you want to generate: ", "int"]
    }
    
    def __init__(self, values):
        self.n_data = values[0]
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            Id = uuid4()
            data.append(Id)
            
        return data
    
class IPv4:
    fields = {
        "n_data": ["Enter the numbe of data you want to generate: ", "int"]
    }
    
    def __init__(self, values):
        self.n_data = values[0]
        
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
    
class Continuous:
    fields = {
        "range_start": ["Enter the start of the range: ", "float"],
        "range_end": ["Enter the end of the range", "float"],
        "n_decimal": ["Enter the number of decimals after '.': ", "int"],
        "n_data": ["Enter the number of data you want to generate: ", "int"]
    }
    
    def __init__(self, values):
        self.range_start = values[0]
        self.range_end = values[1]
        self.n_decimal = values[2]
        self.n_data = values[3]
        
    def create_list(self):
        numbers_list = []
        for i in range(self.n_data):
            number = round(random.uniform(self.range_start, self.range_end), self.n_decimal)
            numbers_list.append(number)
        return numbers_list
    
class Discrete:
    fields = {
        "range_start": ["Enter the start of the range: ", "int"],
        "range_end": ["Enter the end of the range: ", "int"],
        "n_data": ["Enter the number of data you want to generate: ", "int"]
    }
    
    def __init__(self, values):
        self.range_start = values[0]
        self.range_end = values[1]
        self.n_data = values[2]
        
    def create_list(self):
        numbers_list = []
        for i in range(self.n_data):
            number = random.randint(self.range_start, self.range_end)
            numbers_list.append(number)
        return numbers_list
    
class Phone:
    constants = ["0917", "0936", "0938", "0939"]
    numbers = [str(x) for x in digits]
    
    fields = {
        "n_data": ["Enter the numbe of data you want to generate: ", "int"]
    }
    
    def __init__(self, values):
        self.n_data = values[0]
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            phone_number = random.choice(Phone.constants)
            for j in range(7):
                phone_number += random.choice(Phone.numbers)
            data.append(phone_number)
            
        return data
    
class Time:
    fields = {
        "n_data": ["Enter the numbe of data you want to generate: ", "int"]
    }
    
    def __init__(self, values):
        self.n_data = values[0]
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            time = datetime.time(hour=random.randint(0, 23), minute=random.randint(0, 59), second=random.randint(0,59))
            data.append(time)
        
        return data