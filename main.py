from src import Categorized
from src import Date
from src import Email
from src import ID
from src import IPv4
from src import Number
from src import Phone
from src import Time

def main():
    print("\n1. Create a new random list\n2. exit\n")
    action = int(input())
    
    if action == 2:
        exit()
        
    print("\nWhat type of data you want to generate? Pleas select by typing the number:")
    print("1.Categorized data\n2.Date\n3.Unique IDs\n4.IPv4\n5.Number\n6.Phone Number\n7.Random Time\n8.Random Email\n")
    data_type = int(input())
    
    match data_type:
        case 1:
            values = Categorized.Categorized.get_fields()
            RDG = Categorized.Categorized(values)
            for data in RDG.create_list():
                print(data)
        case 2:
            values = Date.Date.get_fields()
            RDG = Date.Date(values)
            for data in RDG.create_list():
                print(data)
        case 3:
            value = ID.ID.get_fields()
            RDG = ID.ID(value)
            for data in RDG.create_list():
                print(data)
        case 4:
            value = IPv4.IPv4.get_fields()
            RDG = IPv4.IPv4(value)
            for data in RDG.create_list():
                print(data)
        case 5:
            print("Number")
        case 6:
            print("Phone")
        case 7:
            print("Time")
        case 8:
            print("Email")
            
            
if __name__ == "__main__":
    print("\nWelcome to Random Data Generator. Please choose your action from the options below by typing the number:")
    while True:
        main()