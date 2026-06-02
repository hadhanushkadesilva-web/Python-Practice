# Start with an empty shopping list
shopping = []
print(f"Empty list: {shopping}")

# Add 4 items
shopping.append("Bread")
shopping.append("Eggs")
shopping.append("Milk")
shopping.append("Apples")
print(f"After 4 appends: {shopping}")

# Insert "Tea" at the top
shopping.insert(0, "Tea")
print(f"After insert: {shopping}")

# Remove "Eggs"
shopping.remove("Eggs")
print(f"After remove: {shopping}")

# Pop the last item and save it
removed_item = shopping.pop()
print(f"Removed item: {removed_item}")
print(f"After pop: {shopping}")

# Sort alphabetically
shopping.sort()
print(f"Sorted: {shopping}")

# Final length
print(f"Final length: {len(shopping)}")