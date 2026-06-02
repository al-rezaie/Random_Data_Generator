import random
import datetime
import string
from string import digits
from uuid import uuid4

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
        
        return [categories_list, n_data]
    
class Date:
    date_format = "%d-%m-%Y"
    
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
        start_date = datetime.datetime.strptime(string_start_date, Date.date_format)
        
        string_end_date = input("Enter the end date: ")
        end_date = datetime.datetime.strptime(string_end_date, Date.date_format)
        
        n_data = int(input("Enter the number of data you want to generate: "))
        
        return [start_date, end_date, n_data]
    
class Email:
    characters = string.ascii_letters + string.digits
    prefixes = ["@gmail.com", "@yahoo.com", "@outlook.com"]
    def __init__(self, n_data):
        self.n_data = n_data
        
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
    
    def get_fields(*args):
        n_data = int(input("Enter the number of data you want to generate: "))
        
        return n_data
    
class ID:
    def __init__(self, n_data):
        self.n_data = n_data
        
    def create_list(self):
        data = []
        for i in range(self.n_data):
            Id = uuid4()
            data.append(Id)
            
        return data
    
    def get_fields(*args):
        n_data = int(input("Enter the number of data you want to generate: "))
        
        return n_data
    
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
    
class Continuous:
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
    
    @classmethod
    def get_fields(*args):
        range_start = float(input("Enter the start of the range: "))
        range_end = float(input("Enter the end of the range: "))
        n_decimal = int(input("Enter the number of decimals after '.': "))
        n_data = int(input("Enter the number of data you want to generate: "))
        
        return [range_start, range_end, n_decimal, n_data]
    
class Discrete:
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
    
    @classmethod
    def get_fields(*args):
        range_start = int(input("Enter the start of the range: "))
        range_end = int(input("Enter the end of the range: "))
        n_data = int(input("Enter the number of data you want to generate: "))
        
        return [range_start, range_end, n_data]
    
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
                phone_number += random.choice(Phone.numbers)
            data.append(phone_number)
            
        return data
    
    def get_fields(*args):
        n_data = int(input("Enter the number of data you want to generate: "))
        
        return n_data
    
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