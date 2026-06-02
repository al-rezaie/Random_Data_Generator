import RDGs

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
            values = RDGs.Categorized.get_fields()
            RDG = RDGs.Categorized(values)
            for data in RDG.create_list():
                print(data)
        case 2:
            values = RDGs.Date.get_fields()
            RDG = RDGs.Date(values)
            for data in RDG.create_list():
                print(data)
        case 3:
            value = RDGs.ID.get_fields()
            RDG = RDGs.ID(value)
            for data in RDG.create_list():
                print(data)
        case 4:
            value = RDGs.IPv4.get_fields()
            RDG = RDGs.IPv4(value)
            for data in RDG.create_list():
                print(data)
        case 5:
            print("\nPlease select the number type by typing the number:\n")
            print("1.Decimal\n2.Integer\n")
            number_type = int(input())
            
            if number_type == 1:
                values = RDGs.Continuous.get_fields()
                RDG = RDGs.Continuous(values)
                for data in RDG.create_list():
                    print(data)
            
            else:
                values = RDGs.Discrete.get_fields()
                RDG = RDGs.Discrete(values)
                for data in RDG.create_list():
                    print(data)
            
        case 6:
            value = RDGs.Phone.get_fields()
            RDG = RDGs.Phone(value)
            for data in RDG.create_list():
                print(data)
        case 7:
            value = RDGs.Time.get_fields()
            RDG = RDGs.Time(value)
            for data in RDG.create_list():
                print(data)
        case 8:
            value = RDGs.Email.get_fields()
            RDG = RDGs.Email(value)
            for data in RDG.create_list():
                print(data)
            
            
if __name__ == "__main__":
    print("\nWelcome to Random Data Generator. Please choose your action from the options below by typing the number:")
    while True:
        main()