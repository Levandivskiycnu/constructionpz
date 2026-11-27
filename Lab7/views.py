
class TaskView:

    def show_menu(self):
        print("\n========== TODO LIST ==========")
        print("1. Створити завдання")
        print("2. Змінити статус завдання")
        print("3. Видалити завдання")
        print("4. Редагувати завдання")
        print("5. Показати всі завдання")
        print("6. Фільтрувати за статусом")
        print("7. Знайти завдання за ID")
        print("0. Вийти")

    def get_choice(self):
        return input("Ваш вибір: ")

    def show_tasks(self, tasks):
        if not tasks:
            print("Завдань немає.")
            return

        print("\n" + "-" * 105)
        print(f"{'ID':36} | {'ОПИС':20} | {'СТАТУС':12} | {'ЧАС'}")
        print("-" * 105)

        for task in tasks:
            scheduled = task.scheduled_at.strftime("%d.%m.%Y %H:%M") if task.scheduled_at else "-"
            print(f"{str(task.id):36} | {task.description[:20]:20} | {task.status:12} | {scheduled}")

        print("-" * 105)

    def show_message(self, message):
        print(message)

    def get_description(self):
        return input("Введіть опис завдання: ")

    def get_id(self):
        return input("Введіть ID завдання: ")

    def get_status(self):
        print("1. ToDo")
        print("2. InProgress")
        print("3. Done")

        choice = input("Оберіть статус: ")

        statuses = {
            "1": "ToDo",
            "2": "InProgress",
            "3": "Done"
        }

        return statuses.get(choice)

    def get_schedule(self):
        value = input("Введіть дату та час (ДД.ММ.РРРР ГГ:ХХ), або Enter: ")

        if not value:
            return None

        try:
            return datetime.strptime(value, "%d.%m.%Y %H:%M")
        except ValueError:
            self.show_message("Неправильний формат дати!")
            return None


from datetime import datetime
