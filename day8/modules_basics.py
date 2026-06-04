# Way 1 — import the whole module
import math
print(math.pi)            # 3.141592653589793
print(math.sqrt(16))      # 4.0

# Way 2 — import specific things from the module
from math import pi, sqrt
print(pi)                  # 3.141592653589793 (no math. prefix needed)
print(sqrt(16))            # 4.0

# Way 3 — import with an alias (rename for convenience)
import random as rnd
print(rnd.randint(1, 100))    # random number between 1 and 100
#-----------------------
# 1. math — calculate something
import math

print(f"Pi is approximately {math.pi:.4f}")
print(f"Square root of 144 is {math.sqrt(144)}")
print(f"3 to the power of 4 is {math.pow(3, 4)}")

# 2. random — pick / shuffle / random number
import random

print(f"\nRandom number 1 to 100: {random.randint(1, 100)}")

fruits = ["apple", "banana", "cherry", "mango", "grape"]
print(f"Random fruit: {random.choice(fruits)}")

random.shuffle(fruits)
print(f"Shuffled list: {fruits}")

# 3. datetime — current date and time
from datetime import datetime, date

today = date.today()
print(f"\nToday's date: {today}")

now = datetime.now()
print(f"Right now: {now}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")

# 4. os — check file existence (already used)
import os

print(f"\nDo I have a notes.json? {os.path.exists('notes.json')}")
print(f"What's the current working directory? {os.getcwd()}")