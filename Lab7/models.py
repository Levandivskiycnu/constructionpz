
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime


@dataclass
class Task:
    id: UUID = field(default_factory=uuid4)
    description: str = ""
    status: str = "ToDo"
    scheduled_at: datetime = None


class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, scheduled_at=None):
        task = Task(description=description, scheduled_at=scheduled_at)
        self.tasks.append(task)
        return task

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def update_task(self, task_id, description):
        task = self.get_task(task_id)
        if task:
            task.description = description
            return True
        return False

    def change_status(self, task_id, status):
        task = self.get_task(task_id)
        if task and status in ["ToDo", "InProgress", "Done"]:
            task.status = status
            return True
        return False

    def get_all_tasks(self):
        return self.tasks

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    def get_task(self, task_id):
        try:
            task_id = UUID(str(task_id))
        except ValueError:
            return None

        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
