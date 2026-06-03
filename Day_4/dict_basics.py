# Create a dictionary about yourself
person = {
    "name": "Dhanushka",
    "age": 35,
    "country": "Sri Lanka",
    "occupation": "Data Engineer"
}

# 1. Print just the name
print(person["name"])

# 2. Print the country
print(person["country"])

# 3. Change the age to 36
person["age"] = 36
print(person)

# 4. Add a new key "hobby" with value "Cricket"
person["hobby"] = "Cricket"
print(person)

# 5. Check if "email" is a key
if "email" in person:
    print("Has email")
else:
    print("No email yet")

# 6. Print how many keys the dictionary has
print(f"Total fields: {len(person)}")

# 7. Remove the country
del person["country"]
print(person)