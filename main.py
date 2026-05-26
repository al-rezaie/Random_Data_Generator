from src import Number

D_type = input("Descrete (D) or Continuous (C)? ")

match D_type:
    case "D":
        generator = Number.Discrete(0, 20, 50)
    case "C":
        generator = Number.Continuous(0, 20, 5, 80)
        
for i in generator.create_list():
    print(i)