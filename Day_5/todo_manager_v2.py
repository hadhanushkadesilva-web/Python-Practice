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


# Main code — short and readable
tasks = []
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
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")