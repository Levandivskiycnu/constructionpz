
import unittest

from employee import (
    Employee,
    HourlyEmployee,
    FixedSalaryEmployee,
    FOPEmployee,
    SelfEmployedContractor,
    sort_employees
)


class TestEmployees(unittest.TestCase):

    def test_hourly_salary(self):
        worker = HourlyEmployee("Коваль", "Олег", 250, 160)

        self.assertEqual(
            worker.average_monthly_salary(),
            40000
        )

    def test_fixed_salary(self):
        worker = FixedSalaryEmployee(
            "Бондар", "Ірина", 35000
        )

        self.assertEqual(
            worker.average_monthly_salary(),
            35000
        )

    def test_hourly_taxes(self):
        worker = HourlyEmployee("Коваль", "Олег", 250, 160)

        self.assertEqual(
            worker.calculate_taxes(),
            {
                "ПДФО": 7200.0,
                "ВЗ": 600.0,
                "ЄСВ": 1760
            }
        )

    def test_fop_taxes(self):
        worker = FOPEmployee("Мельник", "Андрій", 300, 160)

        self.assertEqual(
            worker.calculate_taxes(),
            {
                "ЄП": 2400.0,
                "ЄСВ": 1760
            }
        )

    def test_contractor_taxes(self):
        worker = SelfEmployedContractor(
            "Шевченко", "Марія", 40000
        )

        self.assertEqual(
            worker.calculate_taxes(),
            {
                "ЄП": 2000.0,
                "ЄСВ": 1760
            }
        )

    def test_sorting(self):
        workers = [
            FixedSalaryEmployee("Шевченко", "Марія", 40000),
            FixedSalaryEmployee("Бондар", "Ірина", 35000)
        ]

        result = sort_employees(workers)

        self.assertEqual(
            [worker.surname for worker in result],
            ["Бондар", "Шевченко"]
        )

    def test_base_class_is_abstract(self):
        with self.assertRaises(TypeError):
            Employee("Тест", "Тест")


if __name__ == "__main__":
    unittest.main()
