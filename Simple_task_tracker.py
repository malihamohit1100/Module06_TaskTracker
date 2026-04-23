import json


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        title = input("Enter Title: ").strip()
        description = input("Enter Description: ").strip()

        task = {
            "title": title,
            "description": description
        }

        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
            return

        print("\nTasks:")
        print("------")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['title']} - {task['description']}")
        print()

    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete.\n")
            return

        self.view_tasks()

        try:
            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(self.tasks):
                deleted_task = self.tasks.pop(task_number - 1)
                self.save_tasks()
                print(f"Task '{deleted_task['title']}' deleted successfully!\n")
            else:
                print("Invalid task number.\n")

        except ValueError:
            print("Please enter a valid number.\n")

    def run(self):
        while True:
            print("===== Task Tracker =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                print("Exiting Task Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    manager = TaskManager()
    manager.run()





        