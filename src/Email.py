import random
import string

class Email:
    characters = string.ascii_letters + string.digits
    prefixes = ["@gmail.com", "@yahoo.com", "@outlook.com"]
    def __init__(self, n_data):
        self.n_data = n_data
        
    def ceate_list(self):
        data = []
        for i in range(self.n_data):
            n_characters = random.randint(3, 11)
            email_characters = random.choices(Email.characters, k=n_characters)
            email = ""
            for c in email_characters:
                email + c
            email + random.choice(Email.prefixes)
            data.append(email)
            
        return data