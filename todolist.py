import json
import os

FILE_NAME = "todos.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['task']}")


def complete_task(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


def delete_task(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks()

        elif choice == "2":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "3":
            view_tasks()
            task_num = int(input("Enter task number to complete: ")) - 1
            complete_task(task_num)

        elif choice == "4":
            view_tasks()
            task_num = int(input("Enter task number to delete: ")) - 1
            delete_task(task_num)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()