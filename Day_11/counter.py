class Counter:
    def __init__(self, initial_value=0):
        self.__count = initial_value  # private attribute

    def increment(self):
        self.__count += 1

    def get_count(self):
        return self.__count
    
    def reset(self):
        self.__count = 0
    
    def __str__(self):
        return f"Counter value: {self.__count}"
    
# Test code
c = Counter()
print(c)              # Counter at 0
c.increment()
c.increment()
c.increment()
print(c.get_count())  # 3
print(c)              # Counter at 3
c.reset()
print(c)              # Counter at 0

# Try to access __count directly — should fail
try:
    print(c.__count)
except AttributeError as e:
    print(f"Can't access private: {e}")