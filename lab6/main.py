
import argparse
from faker import Faker

from employee import (
    HourlyEmployee,
    FixedSalaryEmployee,
    FOPEmployee,
    SelfEmployedContractor,
    sort_employees
)

fake = Faker("uk_UA")


def generate_employees(count):
    employees = []

    for index in range(count):
        surname = fake.last_name()
        name = fake.first_name()

        # Почергово створюємо чотири типи працівників
        if index % 4 == 0:
            employee = HourlyEmployee(
                surname, name, 250, 160
            )

        elif index % 4 == 1:
            employee = FixedSalaryEmployee(
                surname, name, 35000
            )

        elif index % 4 == 2:
            employee = FOPEmployee(
                surname, name, 300, 160
            )

        else:
            employee = SelfEmployedContractor(
                surname, name, 40000
            )

        employees.append(employee)

    return sort_employees(employees)


def show_employees(employees):
    for employee in employees:
        print(employee)


def main():
    parser = argparse.ArgumentParser(
        description="Облік працівників IT-підприємства"
    )

    commands = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Команда генерації працівників
    generate = commands.add_parser(
        "generate",
        help="Згенерувати працівників"
    )

    generate.add_argument(
        "--count",
        type=int,
        default=8,
        help="Кількість працівників"
    )

    # Демонстраційна команда
    commands.add_parser(
        "demo",
        help="Показати приклад усіх типів працівників"
    )

    args = parser.parse_args()

    if args.command == "generate":

        if args.count < 1:
            parser.error("Кількість має бути більше нуля")

        employees = generate_employees(args.count)
        show_employees(employees)

    elif args.command == "demo":

        employees = [
            HourlyEmployee("Коваль", "Олег", 250, 160),
            FixedSalaryEmployee("Бондар", "Ірина", 35000),
            FOPEmployee("Мельник", "Андрій", 300, 160),
            SelfEmployedContractor(
                "Шевченко", "Марія", 40000
            )
        ]

        employees = sort_employees(employees)
        show_employees(employees)


if __name__ == "__main__":
    main()
