tasks = []

while True:
    print("=== TO-DO LIST MANAGER ===")
    print("1. Add a task")
    print("2. Show all tasks")
    print("3. Remove a task")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        # show tasks: loop over tasks with enumerate(start=1)
        # special case: if list is empty, print "(No tasks yet.)"
        if not tasks:
            print("(No tasks yet.)")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        # remove a task:
        # show the numbered tasks first so user can see
        # ask: "Enter task number to remove: "  → int(input(...))
        # then tasks.pop(number - 1)   ← subtract 1 because user counts from 1
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        remove_task_num = int(input("Enter task number to remove: "))
        if 1 <= remove_task_num <= len(tasks):
            removed_task = tasks.pop(remove_task_num - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")