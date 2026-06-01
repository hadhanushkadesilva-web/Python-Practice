# Test 1 — driving check (both required)
age = 20
has_license = True
if age >= 18 and has_license:
    print("Can drive.")
else:
    print("Cannot drive.")

# Test 2 — driving check (one missing)
age = 20
has_license = False
if age >= 18 and has_license:
    print("Can drive.")
else:
    print("Cannot drive.")

# Test 3 — discount (member or big amount)
amount = 50
is_member = True
if amount > 100 or is_member:
    print("Discount applied.")
else:
    print("No discount.")

# Test 4 — login check (not logged in)
is_logged_in = False
if not is_logged_in:
    print("Please log in.")
else:
    print("Welcome back.")