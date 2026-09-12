# Task 3: Create a console application for basic CRUD operations
# Objective: Implement Create, Read, Update, and Delete operations using lists for data storage.

class Task:
    """Class to define task attributes."""

    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = "Pending"  # Default status

    def __str__(self):
        return f"ID: {self.task_id} | Title: {self.title} | Status: {self.status}\nDescription: {self.description}"


class TaskManager:
    """Class to handle all CRUD operations."""

    def __init__(self):
        # List to store task objects
        self.tasks = []
        self.next_id = 1

    # 1. CREATE Operation
    def create_task(self, title, description):
        new_task = Task(self.next_id, title, description)
        self.tasks.append(new_task)
        print(f"\n✅ Task '{title}' created successfully with ID: {self.next_id}")
        self.next_id += 1

    # 2. READ Operation
    def read_tasks(self):
        if not self.tasks:
            print("\n📂 No tasks available to display.")
            return
        print("\n--- 📋 Current Task List ---")
        for task in self.tasks:
            print("-" * 30)
            print(task)
        print("-" * 30)

    # 3. UPDATE Operation
    def update_task(self, task_id, new_title, new_description, new_status):
        for task in self.tasks:
            if task.task_id == task_id:

                task.title = new_title if new_title else task.title
                task.description = new_description if new_description else task.description
                task.status = new_status if new_status else task.status
                print(f"\n✅ Task ID {task_id} updated successfully.")
                return
        print(f"\n❌ Task with ID {task_id} not found.")

    # 4. DELETE Operation
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"\n🗑️ Task ID {task_id} deleted successfully.")
                return
        print(f"\n❌ Task with ID {task_id} not found.")


def main():
    manager = TaskManager()

    while True:
        print("\n==============================")
        print("      CRUD TASK MANAGER       ")
        print("==============================")
        print("1. Add a New Task (Create)")
        print("2. View All Tasks (Read)")
        print("3. Edit a Task (Update)")
        print("4. Remove a Task (Delete)")
        print("5. Exit Application")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            title = input("Enter Task Title: ")
            desc = input("Enter Task Description: ")
            manager.create_task(title, desc)

        elif choice == '2':
            manager.read_tasks()

        elif choice == '3':
            try:
                task_id = int(input("Enter Task ID to update: "))
                print("(Press Enter to skip updating a specific field)")
                new_title = input("Enter new Title: ")
                new_desc = input("Enter new Description: ")
                new_status = input("Enter new Status (e.g., Completed): ")
                manager.update_task(task_id, new_title, new_desc, new_status)
            except ValueError:
                print("\n❌ Invalid input! Task ID must be a number.")

        elif choice == '4':
            try:
                task_id = int(input("Enter Task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("\n❌ Invalid input! Task ID must be a number.")

        elif choice == '5':
            print("\n👋 Exiting the Task Manager. Goodbye!")
            break

        else:
            print("\n❌ Invalid choice! Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()