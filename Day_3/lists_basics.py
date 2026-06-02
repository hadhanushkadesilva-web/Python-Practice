fruits = ["apple", "banana", "cherry", "mango"]
numbers = [10, 20, 30, 40, 50]
mixed = ["hello", 42, 3.14, True]   # lists can hold ANY type, even mixed
empty = []                            # an empty list

print(fruits[0])   # 'apple'  ← first item
print(fruits[2])   # 'cherry' ← third item
print(fruits[-1])  # 'mango'  ← last item (negative index)

print(fruits[0:2])   # ['apple', 'banana']         ← first 2
print(fruits[1:])    # ['banana', 'cherry', 'mango']  ← from index 1 to end
print(fruits[-2:])   # ['cherry', 'mango']          ← last 2

print(len(fruits))   # 4

#______________
# Create a list of 5 cities you'd like to visit
cities = ["Tokyo", "Paris", "London", "Sydney", "Cairo"]

# 1. Print the first city
print(cities[0])

# 2. Print the third city
print(cities[2])

# 3. Print the last city using negative indexing
print(cities[-1])

# 4. Print the first 3 cities (slice)
print(cities[0:3])

# 5. Print the length of the list
print(len(cities))

# 6. Change the second city to "Rome"
cities[1] = "Rome"
print(cities)

# 7. Print how many cities are in the list after changing
print(len(cities))