
from models import TaskModel
from views import TaskView
from controllers import TaskController


def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    while True:
        view.show_menu()
        choice = view.get_choice()

        if choice == "1":
            controller.create_task()
        elif choice == "2":
            controller.change_status()
        elif choice == "3":
            controller.delete_task()
        elif choice == "4":
            controller.update_task()
        elif choice == "5":
            controller.show_all_tasks()
        elif choice == "6":
            controller.filter_tasks()
        elif choice == "7":
            controller.find_task()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Неправильний вибір!")


if __name__ == "__main__":
    main()
