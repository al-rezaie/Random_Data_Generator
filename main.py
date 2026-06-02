import RDGs
from datetime import datetime

def get_fields(fields: dict):
    while True:
        error = False
        values = []
    
        for key in fields.keys():
            field = fields[key]
            user_input = input(field[0])
            
            try:   
                match field[1]:
                    case "int":
                        values.append(int(user_input))
                    
                    case "float":
                        values.append(float(user_input))
                    
                    case "list":
                        values.append(user_input.strip().split(","))
                    
                    case "date":
                        values.append(datetime.strptime(user_input, RDGs.Date.date_format))
                        
            except:
                print("\nYour input doesn't match the format. Please try again.\n")
                error = True
                break
            
        if error:
            continue
        else:
            return values

def main():
    print("\n1. Create a new random list\n2. exit\n")
    
    while True:
        try:
            action = int(input())
            break
        except:
            print("\nYour input doesn't match the pattern. Please try again.\n")
            continue
    
    if action == 2:
        exit()
        
    print("\nWhat type of data you want to generate? Pleas select by typing the number:")
    print("1.Categorized data\n2.Date\n3.Unique IDs\n4.IPv4\n5.Number\n6.Phone Number\n7.Random Time\n8.Random Email\n")
    
    while True:
        try:
            data_type = int(input())
            break
        except:
            print("\nYour input doesn't match the pattern. Please try again.\n")
            continue
    
    match data_type:
        case 1:
            values = get_fields(RDGs.Categorized.fields)
            RDG = RDGs.Categorized(values)
            for data in RDG.create_list():
                print(data)
        case 2:
            values = get_fields(RDGs.Date.fields)
            RDG = RDGs.Date(values)
            for data in RDG.create_list():
                print(data)
        case 3:
            values = get_fields(RDGs.ID.fields)
            RDG = RDGs.ID(values)
            for data in RDG.create_list():
                print(data)
        case 4:
            values = get_fields(RDGs.IPv4.fields)
            RDG = RDGs.IPv4(values)
            for data in RDG.create_list():
                print(data)
        case 5:
            print("\nPlease select the number type by typing the number:\n")
            print("1.Decimal\n2.Integer\n")
            
            while True:
                try:
                    number_type = int(input())
                    if number_type > 2 or number_type < 1:
                        raise "Invalid entry"
                    break
                except:
                    print("\nYour input doesn't match the pattern. Please try again.\n")
                    continue
            
            if number_type == 1:
                values = get_fields(RDGs.Continuous.fields)
                RDG = RDGs.Continuous(values)
                for data in RDG.create_list():
                    print(data)
            
            else:
                values = get_fields(RDGs.Discrete.fields)
                RDG = RDGs.Discrete(values)
                for data in RDG.create_list():
                    print(data)
            
        case 6:
            values = get_fields(RDGs.Phone.fields)
            RDG = RDGs.Phone(values)
            for data in RDG.create_list():
                print(data)
                
        case 7:
            values = get_fields(RDGs.Time.fields)
            RDG = RDGs.Time(values)
            for data in RDG.create_list():
                print(data)
                
        case 8:
            values = get_fields(RDGs.Email.fields)
            RDG = RDGs.Email(values)
            for data in RDG.create_list():
                print(data)
            
            
if __name__ == "__main__":
    print("\nWelcome to Random Data Generator. Please choose your action from the options below by typing the number:")
    while True:
        main()