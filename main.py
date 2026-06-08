from datetime import datetime
from pyperclip import copy
from enum import Enum
import RDGs

GENERATORS = {
    1: ("Categorized Data", RDGs.Categorized),
    2: ("Date", RDGs.Date),
    3: ("Unique IDs", RDGs.ID),
    4: ("IPv4", RDGs.IPv4),
    5: ("Phone Number", RDGs.Phone),
    6: ("Random Time", RDGs.Time),
    7: ("Random Email", RDGs.Email),
}

class Colors(Enum):
    Info = "\033[96m"
    Reset = "\033[0m"

def get_fields(fields: dict):
    values = []

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
                    "\nInvalid input."
                    "\nPlease try again.\n"
                )

    return values


def print_list(data):
    print()

    for item in data:
        print(item)

    print()

def copy_to_clipboard(data):
    print("\nDo you want the data to be copied?\n")
    print("0.No\n1.Yes\n")
    confirm = input("Select number: ").strip()
    
    if confirm == "1": 
        copy("\n".join(str(d) for d in data))
        print(f"\n{Colors.Info.value}Data was copied{Colors.Reset.value}\n")


def run_generator(generator_class):
    try:
        values = get_fields(generator_class.fields)
        generator = generator_class(values)
        data_list = generator.create_list()
        print_list(data_list)
        copy_to_clipboard(data_list)

    except ValueError as e:
        print(f"\nError: {e}\n")


def main():

    while True:

        print("\n1. Create a new random list")
        print("2. Exit\n")

        try:
            action = int(input("Select option: "))

            if action == 2:
                break

            if action != 1:
                raise ValueError

        except ValueError:
            print("\nInvalid option.\n")
            continue

        print("\nSelect data type:\n")

        for key, (name, _) in GENERATORS.items():
            print(f"{key}. {name}")

        print("8. Number")

        try:
            data_type = int(input("\nSelect option: "))

        except ValueError:
            print("\nInvalid option.\n")
            continue

        if data_type == 8:
            while True:
                print("\n1. Decimal")
                print("2. Integer\n")

                try:
                    number_type = int(
                        input("Select option: ")
                    )

                    if number_type == 1:
                        run_generator(RDGs.Continuous)

                    elif number_type == 2:
                        run_generator(RDGs.Discrete)

                    else:
                        print("\nInvalid option.\n")
                        
                    break

                except ValueError:
                    print("\nInvalid option.\n")
                    
            continue

        if data_type not in GENERATORS:
            print("\nInvalid option.\n")
            continue

        run_generator(
            GENERATORS[data_type][1]
        )


if __name__ == "__main__":

    print(
        "\nWelcome to Random Data Generator"
    )

    main()