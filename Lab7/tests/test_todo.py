
import unittest
from models import TaskModel


class TestTaskModel(unittest.TestCase):

    def setUp(self):
        self.model = TaskModel()
        self.task = self.model.add_task("Вивчити Python")

    def test_add_task(self):
        self.assertEqual(len(self.model.tasks), 1)
        self.assertEqual(self.task.description, "Вивчити Python")
        self.assertEqual(self.task.status, "ToDo")

    def test_delete_task(self):
        result = self.model.delete_task(self.task.id)

        self.assertTrue(result)
        self.assertEqual(len(self.model.tasks), 0)

    def test_delete_nonexistent_task(self):
        result = self.model.delete_task("00000000-0000-0000-0000-000000000000")

        self.assertFalse(result)

    def test_update_task(self):
        result = self.model.update_task(self.task.id, "Вивчити Java")

        self.assertTrue(result)
        self.assertEqual(self.task.description, "Вивчити Java")

    def test_update_nonexistent_task(self):
        result = self.model.update_task("invalid-id", "Нове завдання")

        self.assertFalse(result)

    def test_change_status(self):
        result = self.model.change_status(self.task.id, "InProgress")

        self.assertTrue(result)
        self.assertEqual(self.task.status, "InProgress")

    def test_invalid_status(self):
        result = self.model.change_status(self.task.id, "Unknown")

        self.assertFalse(result)

    def test_get_all_tasks(self):
        tasks = self.model.get_all_tasks()

        self.assertEqual(len(tasks), 1)

    def test_filter_by_status(self):
        self.model.add_task("Зробити лабораторну")
        self.model.change_status(self.task.id, "Done")

        tasks = self.model.get_tasks_by_status("Done")

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].status, "Done")

    def test_get_task(self):
        task = self.model.get_task(self.task.id)

        self.assertEqual(task.description, "Вивчити Python")

    def test_get_nonexistent_task(self):
        task = self.model.get_task("00000000-0000-0000-0000-000000000000")

        self.assertIsNone(task)


if __name__ == "__main__":
    unittest.main()
