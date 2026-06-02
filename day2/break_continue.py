# Loop 1 — break: stop at the first negative number
print("Loop 1:")
numbers = [3, 8, 12, -4, 25, -7, 9]
for n in numbers:
    if n < 0:
        print(f"Found a negative: {n}. Stopping.")
        break
    print(f"Positive: {n}")

# Loop 2 — continue: skip multiples of 3
print("Loop 2:")
for i in range(1, 11):
    if i % 3 == 0:        # i is a multiple of 3 (3, 6, 9)
        continue
    print(i)

# Loop 3 — both together: find first even number > 10
print("Loop 3:")
candidates = [3, 5, 7, 9, 4, 6, 12, 14]
for x in candidates:
    if x % 2 != 0:        # odd → skip
        continue
    if x > 10:            # even AND > 10 → found it!
        print(f"First even number over 10: {x}")
        break
    print(f"Skipped even but small: {x}")