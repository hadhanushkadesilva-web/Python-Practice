# Part 1 — remove duplicates from a list
print("Part 1: Removing duplicates")
votes = ["red", "blue", "red", "green", "blue", "red"]
unique_votes = set(votes)
print(f"All votes: {votes}")
print(f"Unique colors voted for: {unique_votes}")
print(f"Number of unique colors: {len(unique_votes)}")

# Part 2 — basic set operations
print("\nPart 2: Set operations")
team_a = {"Anna", "Bob", "Cathy", "David"}
team_b = {"Bob", "Cathy", "Eve", "Frank"}

print(f"Everyone (union):       {team_a | team_b}")
print(f"In both (intersection): {team_a & team_b}")
print(f"Only in team_a:         {team_a - team_b}")
print(f"Only in team_b:         {team_b - team_a}")

# Part 3 — fast membership test
print("\nPart 3: Quick checks")
languages = {"Python", "JavaScript", "Go", "Rust"}
if "Python" in languages:
    print("✓ We know Python")
if "PHP" in languages:
    print("✓ We know PHP")
else:
    print("✗ We don't know PHP")