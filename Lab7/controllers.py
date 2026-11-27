
class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_task(self):
        description = self.view.get_description()

        if not description.strip():
            self.view.show_message("Опис не може бути порожнім!")
            return

        scheduled_at = self.view.get_schedule()
        task = self.model.add_task(description, scheduled_at)

        self.view.show_message(f"Завдання створено! ID: {task.id}")

    def delete_task(self):
        task_id = self.view.get_id()

        if self.model.delete_task(task_id):
            self.view.show_message("Завдання видалено!")
        else:
            self.view.show_message("Завдання не знайдено!")

    def update_task(self):
        task_id = self.view.get_id()
        description = self.view.get_description()

        if not description.strip():
            self.view.show_message("Опис не може бути порожнім!")
            return

        if self.model.update_task(task_id, description):
            self.view.show_message("Завдання оновлено!")
        else:
            self.view.show_message("Завдання не знайдено!")

    def change_status(self):
        task_id = self.view.get_id()
        status = self.view.get_status()

        if status is None:
            self.view.show_message("Неправильний статус!")
            return

        if self.model.change_status(task_id, status):
            self.view.show_message("Статус змінено!")
        else:
            self.view.show_message("Завдання не знайдено!")

    def show_all_tasks(self):
        self.view.show_tasks(self.model.get_all_tasks())

    def filter_tasks(self):
        status = self.view.get_status()

        if status is None:
            self.view.show_message("Неправильний статус!")
            return

        tasks = self.model.get_tasks_by_status(status)
        self.view.show_tasks(tasks)

    def find_task(self):
        task_id = self.view.get_id()
        task = self.model.get_task(task_id)

        if task:
            self.view.show_tasks([task])
        else:
            self.view.show_message("Завдання не знайдено!")
