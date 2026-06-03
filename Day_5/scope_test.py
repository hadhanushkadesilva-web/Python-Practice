def show_number():
    secret = 99            # local
    print(f"Inside function: secret = {secret}")

show_number()
print(f"Outside function: secret = {secret}")    # ← this line should ERROR