
from abc import ABC, abstractmethod

# Податкові ставки
PIT = 0.18
MILITARY = 0.015
SINGLE_TAX = 0.05
ESV = 1760


class Employee(ABC):
    """Базовий клас працівника."""

    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    @abstractmethod
    def average_monthly_salary(self):
        pass

    @abstractmethod
    def calculate_taxes(self):
        pass

    def net_salary(self):
        salary = self.average_monthly_salary()
        taxes = self.calculate_taxes()

        deductions = (
            taxes.get("ПДФО", 0)
            + taxes.get("ВЗ", 0)
            + taxes.get("ЄП", 0)
        )

        # ЄСВ самостійно сплачують ФОП та самозайняті
        if isinstance(self, (FOPEmployee, SelfEmployedContractor)):
            deductions += taxes.get("ЄСВ", 0)

        return round(salary - deductions, 2)

    def __str__(self):
        return (
            f"{self.surname} {self.name}\n"
            f"Зарплата: {self.average_monthly_salary():.2f} грн\n"
            f"Податки: {self.calculate_taxes()}\n"
            f"До отримання: {self.net_salary():.2f} грн\n"
        )


# 1. Працівник із погодинною оплатою
class HourlyEmployee(Employee):

    def __init__(self, surname, name, hourly_rate, hours_per_month=160):
        super().__init__(surname, name)
        self.hourly_rate = hourly_rate
        self.hours_per_month = hours_per_month

    def average_monthly_salary(self):
        return round(self.hourly_rate * self.hours_per_month, 2)

    def calculate_taxes(self):
        salary = self.average_monthly_salary()

        return {
            "ПДФО": round(salary * PIT, 2),
            "ВЗ": round(salary * MILITARY, 2),
            "ЄСВ": ESV
        }


# 2. Працівник із фіксованою ставкою
class FixedSalaryEmployee(Employee):

    def __init__(self, surname, name, monthly_salary):
        super().__init__(surname, name)
        self.monthly_salary = monthly_salary

    def average_monthly_salary(self):
        return round(self.monthly_salary, 2)

    def calculate_taxes(self):
        salary = self.average_monthly_salary()

        return {
            "ПДФО": round(salary * PIT, 2),
            "ВЗ": round(salary * MILITARY, 2),
            "ЄСВ": ESV
        }


# 3. Погодинний працівник, оформлений як ФОП
class FOPEmployee(Employee):

    def __init__(self, surname, name, hourly_rate, hours_per_month=160):
        super().__init__(surname, name)
        self.hourly_rate = hourly_rate
        self.hours_per_month = hours_per_month

    def average_monthly_salary(self):
        return round(self.hourly_rate * self.hours_per_month, 2)

    def calculate_taxes(self):
        salary = self.average_monthly_salary()

        return {
            "ЄП": round(salary * SINGLE_TAX, 2),
            "ЄСВ": ESV
        }


# 4. Самозайнята особа за цивільно-правовим договором
class SelfEmployedContractor(Employee):

    def __init__(self, surname, name, monthly_contract_amount):
        super().__init__(surname, name)
        self.monthly_contract_amount = monthly_contract_amount

    def average_monthly_salary(self):
        return round(self.monthly_contract_amount, 2)

    def calculate_taxes(self):
        salary = self.average_monthly_salary()

        return {
            "ЄП": round(salary * SINGLE_TAX, 2),
            "ЄСВ": ESV
        }


# Сортування працівників за прізвищем
def sort_employees(employees):
    return sorted(
        employees,
        key=lambda employee: employee.surname.lower()
    )
