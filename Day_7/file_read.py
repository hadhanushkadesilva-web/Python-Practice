# Way 1 — read whole file as one string
print("--- Way 1: read() ---")
with open("my_first_file.txt", "r") as file:
    content = file.read()
    print(content)

# Way 2 — read into a list of lines
print("--- Way 2: readlines() ---")
with open("my_first_file.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Way 3 — loop line-by-line
print("--- Way 3: line-by-line loop ---")
with open("my_first_file.txt", "r") as file:
    for line in file:
        print(line.strip())