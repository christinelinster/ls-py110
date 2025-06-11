# Fibonnaci (Memoization)

memoized = {}
def fibonacci(position):
    if position in memoized:
        return memoized[position]
    
    if position <= 2:
        return 1
    
    result = fibonacci(position - 1) + fibonacci(position - 2)
    memoized[position] = result 

    return result 

    

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True

