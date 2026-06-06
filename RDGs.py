import random
import datetime
import string
from uuid import uuid4


class RandomGenerator:
    fields = {
        "n_data": [
            "Enter the number of data you want to generate: ",
            "int"
        ]
    }

    def __init__(self, values):
        self.n_data = values[-1]

    def create_list(self):
        raise NotImplementedError


class Categorized(RandomGenerator):
    fields = {
        "categories_list": [
            "Enter categories separated by commas: ",
            "list"
        ],
        "n_data": [
            "Enter the number of data you want to generate: ",
            "int"
        ]
    }

    def __init__(self, values):
        self.categories_list = values[0]
        super().__init__(values)

    def create_list(self):
        return [
            random.choice(self.categories_list)
            for _ in range(self.n_data)
        ]


class Date(RandomGenerator):
    date_format = "%d-%m-%Y"

    fields = {
        "start_date": [
            "Enter start date (DD-MM-YYYY): ",
            "date"
        ],
        "end_date": [
            "Enter end date (DD-MM-YYYY): ",
            "date"
        ],
        "n_data": [
            "Enter the number of data you want to generate: ",
            "int"
        ]
    }

    def __init__(self, values):
        self.start_date = values[0]
        self.end_date = values[1]
        super().__init__(values)

        if self.start_date > self.end_date:
            raise ValueError(
                "Start date cannot be greater than end date."
            )

    def create_list(self):
        return [
            (
                self.start_date
                + datetime.timedelta(
                    days=random.randint(
                        0,
                        (self.end_date - self.start_date).days
                    )
                )
            ).date()
            for _ in range(self.n_data)
        ]


class Email(RandomGenerator):
    characters = string.ascii_letters + string.digits

    domains = [
        "@gmail.com",
        "@yahoo.com",
        "@outlook.com"
    ]

    def create_list(self):
        return [
            "".join(
                random.choices(
                    Email.characters,
                    k=random.randint(3, 11)
                )
            )
            + random.choice(Email.domains)
            for _ in range(self.n_data)
        ]


class ID(RandomGenerator):

    def create_list(self):
        return [uuid4() for _ in range(self.n_data)]


class IPv4(RandomGenerator):

    def create_list(self):
        return [
            ".".join(
                str(random.randint(0, 255))
                for _ in range(4)
            )
            for _ in range(self.n_data)
        ]


class Continuous(RandomGenerator):
    fields = {
        "range_start": [
            "Enter the start of the range: ",
            "float"
        ],
        "range_end": [
            "Enter the end of the range: ",
            "float"
        ],
        "n_decimal": [
            "Enter the number of decimal places: ",
            "int"
        ],
        "n_data": [
            "Enter the number of data you want to generate: ",
            "int"
        ]
    }

    def __init__(self, values):
        self.range_start = values[0]
        self.range_end = values[1]
        self.n_decimal = values[2]
        super().__init__(values)

        if self.range_start > self.range_end:
            raise ValueError(
                "Start of range cannot be greater than end."
            )

    def create_list(self):
        return [
            round(
                random.uniform(
                    self.range_start,
                    self.range_end
                ),
                self.n_decimal
            )
            for _ in range(self.n_data)
        ]


class Discrete(RandomGenerator):
    fields = {
        "range_start": [
            "Enter the start of the range: ",
            "int"
        ],
        "range_end": [
            "Enter the end of the range: ",
            "int"
        ],
        "n_data": [
            "Enter the number of data you want to generate: ",
            "int"
        ]
    }

    def __init__(self, values):
        self.range_start = values[0]
        self.range_end = values[1]
        super().__init__(values)

        if self.range_start > self.range_end:
            raise ValueError(
                "Start of range cannot be greater than end."
            )

    def create_list(self):
        return [
            random.randint(
                self.range_start,
                self.range_end
            )
            for _ in range(self.n_data)
        ]


class Phone(RandomGenerator):
    prefixes = [
        "0917",
        "0936",
        "0938",
        "0939"
    ]

    def create_list(self):
        return [
            random.choice(Phone.prefixes)
            + "".join(
                random.choices(
                    string.digits,
                    k=7
                )
            )
            for _ in range(self.n_data)
        ]


class Time(RandomGenerator):

    def create_list(self):
        return [
            datetime.time(
                hour=random.randint(0, 23),
                minute=random.randint(0, 59),
                second=random.randint(0, 59)
            )
            for _ in range(self.n_data)
        ]