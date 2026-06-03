import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file. Return empty list if file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to JSON file with pretty indentation."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# ... your Day 5 functions (print_menu, add_task, show_tasks, remove_task) ...
def print_menu():
    print("=== To-Do List Manager ===")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)

def show_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def remove_task(tasks):
    remove_task_num = int(input("Enter task number to remove: "))
    if 1 <= remove_task_num <= len(tasks):
            removed_task = tasks.pop(remove_task_num - 1)
            print(f"Removed task: {removed_task}")
    else:
            print("Invalid task number.")



# Main code
tasks = load_tasks()
print(f"Loaded {len(tasks)} task(s) from {TASKS_FILE}")

while True:
    print_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        save_tasks(tasks)
        print(f"✓ Saved {len(tasks)} task(s). Goodbye!")
        break
    else:
        print("Invalid choice.")