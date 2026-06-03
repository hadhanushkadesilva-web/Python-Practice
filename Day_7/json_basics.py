import json

# --- Save a dictionary to JSON ---
person = {
    "name": "Dhanushka",
    "age": 35,
    "country": "Sri Lanka",
    "skills": ["Python", "FastAPI", "SQL"],
    "is_student": True
}

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)
print("✓ Wrote person.json")

# --- Read it back ---
with open("person.json", "r") as file:
    loaded = json.load(file)

print(f"\nLoaded data: {loaded}")
print(f"Type: {type(loaded)}")
print(f"Name: {loaded['name']}")
print(f"First skill: {loaded['skills'][0]}")
print(f"How many skills: {len(loaded['skills'])}")

# --- Save a LIST (not dict) ---
tasks = ["Buy groceries", "Pay bills", "Call mom"]
with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)
print("\n✓ Wrote tasks.json")

# --- Read the list back ---
with open("tasks.json", "r") as file:
    loaded_tasks = json.load(file)

print(f"Loaded tasks: {loaded_tasks}")
print(f"Type: {type(loaded_tasks)}")