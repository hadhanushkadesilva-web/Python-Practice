# Loop 1 — coordinates grid
print("Loop 1:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})")

# Loop 2 — small multiplication table (1 to 3)
print("Loop 2:")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row} x {col} = {row * col}")
    print("---")