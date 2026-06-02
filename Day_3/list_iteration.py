# A list of tasks
tasks = ["Buy groceries", "Write report", "Reply to emails", "Go to gym"]

# Method 1 — basic loop (Day 2 style)
print("Basic loop:")
for task in tasks:
    print(task)

# Method 2 — numbered with enumerate (starting at 0)
print("\nNumbered (from 0):")
for index, task in enumerate(tasks):
    print(f"{index}: {task}")

# Method 3 — numbered for humans (starting at 1)
print("\nNumbered (from 1) — ready for users:")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")