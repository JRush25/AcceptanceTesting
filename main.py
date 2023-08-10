class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def list_tasks(self):
        output = "\nTasks"
        for idx, task in enumerate(self.tasks, start=1):
            status = "[Completed]" if task.completed else "[Pending]"
            output += f"\n{idx}.{status} {task.description}"
        return output

    def complete_task(self, task_index):
        print("\nTasks")
        for idx, task in enumerate(self.tasks, start=1):
            if not task.completed:
                print(f"{idx}.{task.description}")
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.completed = True
            print("Task mark as completed:", task.description)
        else:
            print("Invalid task")

    def clear_tasks(self):
        self.tasks = []
        print("***All tasks have been deleted***")

    def list_completed_tasks(self):
        print("\nCompleted Tasks")
        completed_tasks = [task for task in self.tasks if task.completed]
        if completed_tasks:
            for idx, task in enumerate(completed_tasks, start=1):
                print(f"{idx}. {task.description}")
        else:
            print("No tasks have been completed yet.")
def main():
    todo_list_manager = ToDoListManager()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clean the to-do list")
        print("5. Complete task")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            description = input("Input a new task description: ")
            todo_list_manager.add_task(description)
        elif choice == "2":
            print(todo_list_manager.list_tasks())
        elif choice == "3":
            print(todo_list_manager.list_tasks())
            task_index = int(input("Input the task to complete: "))
            todo_list_manager.complete_task(task_index)
        elif choice == "4":
            todo_list_manager.clear_tasks()
        elif choice == "5":
            todo_list_manager.list_completed_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()