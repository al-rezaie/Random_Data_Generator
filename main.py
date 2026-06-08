from datetime import datetime
from pyperclip import copy
from enum import Enum
from pathlib import Path
from csv import writer
import RDGs

GENERATORS = {
    1: ("Categorized", RDGs.Categorized),
    2: ("Date", RDGs.Date),
    3: ("ID", RDGs.ID),
    4: ("IPv4", RDGs.IPv4),
    5: ("Phone Number", RDGs.Phone),
    6: ("Time", RDGs.Time),
    7: ("Email", RDGs.Email),
}

class Colors(Enum):
    Titles = "\033[92m"
    Data = "\033[93m"
    Select = "\033[34m"
    Info = "\033[96m"
    Error = "\033[31m"
    Prompt = "\033[35m"
    Reset = "\033[0m"

def get_fields(fields: dict):
    values = []

    print(Colors.Prompt.value)
    for prompt, data_type in fields.values():

        while True:
            user_input = input(prompt)

            try:
                match data_type:

                    case "int":
                        values.append(int(user_input))

                    case "float":
                        values.append(float(user_input))

                    case "list":
                        values.append(
                            [x.strip()
                             for x in user_input.split(",")]
                        )

                    case "date":
                        values.append(
                            datetime.strptime(
                                user_input,
                                RDGs.Date.date_format
                            )
                        )

                break

            except ValueError:
                print(
                    f"\n{Colors.Error.value}Invalid input."
                    f"\nPlease try again.{Colors.Reset.value}\n"
                )

    return values


def print_list(data):
    print(f"{Colors.Data.value}")

    for item in data:
        print(item)

    print(f"{Colors.Reset.value}")

def copy_to_clipboard(data):
    print(f"\n{Colors.Titles.value}Do you want the data to be copied?{Colors.Reset.value}\n")
    print(f"{Colors.Prompt.value}0.No\n1.Yes{Colors.Reset.value}\n")
    confirm = input(f"{Colors.Select.value}Select number: {Colors.Reset.value}").strip()
    
    if confirm == "1": 
        copy("\n".join(str(d) for d in data))
        print(f"\n{Colors.Info.value}Data was copied{Colors.Reset.value}\n")

def import_to_csv(data, header):
    print(f"\n{Colors.Titles.value}Do you want the data to be saved in a CSV file?\n")
    print(f"{Colors.Prompt.value}0.No\n1.Yes{Colors.Reset.value}\n")
    confirm = input(f"{Colors.Select.value}Select number: {Colors.Reset.value}").strip()
    
    if confirm == "1":    
        file_name = input(f"{Colors.Prompt.value}Please enter the name of the CSV file: {Colors.Reset.value}").strip()
        file_name += ".csv"
        file_address = Path.cwd() / Path(file_name)
        rows = [[d] for d in data]
        print(rows)
        
        try:
            
            with open(file_address, "w", newline="") as csvfile:
                csvwriter = writer(csvfile)
                csvwriter.writerow([header])
                csvwriter.writerows(rows)
                
            print(f"\n{Colors.Info.value}Data was saved{Colors.Reset.value}\n")
            
        except Exception as e:
            print(f"{Colors.Error.value}Something went wrong.")
            print(f"Error: {e}{Colors.Reset.value}")

def run_generator(generator_class, type_name="Number"):
    try:
        values = get_fields(generator_class.fields)
        generator = generator_class(values)
        data_list = generator.create_list()
        print_list(data_list)
        import_to_csv(data_list, type_name)
        copy_to_clipboard(data_list)

    except ValueError as e:
        print(f"\n{Colors.Error.value}Error: {e}{Colors.Reset.value}\n")


def main():

    while True:

        print(f"\n{Colors.Prompt.value}1. Create a new random list")
        print(f"2. Exit{Colors.Reset.value}\n")

        try:
            action = int(input(f"{Colors.Select.value}Select option: {Colors.Reset.value}"))

            if action == 2:
                break

            if action != 1:
                raise ValueError

        except ValueError:
            print(f"\n{Colors.Error.value}Invalid option.{Colors.Reset.value}\n")
            continue

        print(f"\n{Colors.Titles.value}Select data type:\n{Colors.Prompt.value}")

        for key, (name, _) in GENERATORS.items():
            print(f"{key}. {name}")

        print(f"8. Number{Colors.Reset.value}")

        try:
            data_type = int(input(f"\n{Colors.Select.value}Select option: {Colors.Reset.value}"))

        except ValueError:
            print(f"\n{Colors.Error.value}Invalid option.{Colors.Reset.value}\n")
            continue

        if data_type == 8:
            while True:
                print(f"\n{Colors.Prompt.value}1. Decimal")
                print(f"2. Integer{Colors.Reset.value}\n")

                try:
                    number_type = int(
                        input(f"{Colors.Select.value}Select option: {Colors.Reset.value}")
                    )

                    if number_type == 1:
                        run_generator(RDGs.Continuous)

                    elif number_type == 2:
                        run_generator(RDGs.Discrete)

                    else:
                        print(f"\n{Colors.Error.value}Invalid option.{Colors.Reset.value}\n")
                        
                    break

                except ValueError:
                    print(f"\n{Colors.Error.value}Invalid option.{Colors.Reset.value}\n")
                    
            continue

        if data_type not in GENERATORS:
            print(f"\n{Colors.Error.value}Invalid option.{Colors.Reset.value}\n")
            continue

        run_generator(
            GENERATORS[data_type][1],
            GENERATORS[data_type][0]
        )


if __name__ == "__main__":

    print(
        f"\n{Colors.Titles.value}Welcome to Random Data Generator{Colors.Reset.value}"
    )

    main()