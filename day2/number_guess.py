secret_number = 42
max_attempts = 5
attempts = 0

print("🎯 Guess the Number Game")
print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}: "))
    attempts = attempts + 1

    if guess == secret_number:
        print(f"🎉 Correct! You got it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
        
    else:
        print("Too high!")
        

    if attempts == max_attempts:
        print(f"😢 Out of attempts. The number was {secret_number}.")