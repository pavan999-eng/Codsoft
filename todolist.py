import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks in your to-do list!\n")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. [{status}] {task['task']}")

def add_task(tasks):
    task_name = input("\nEnter the task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Task '{removed_task['task']}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1 Add Task")
        print("2 View Tasks")
        print("3 Mark Task as Done")
        print("4 Delete Task")
        print("5 Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
