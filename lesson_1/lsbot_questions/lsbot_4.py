# ​Circular Prime Checker (Advanced)

import math
'''
A circular prime is a prime number that remains 
prime after any cyclic rotation of its digits. 
For example, 197 is a circular prime because all 
its rotations (197, 971, 719) are also prime. 
Create a function that determines if a number is a circular prime.
'''

def is_circular_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        new_number = int(num_str[i:] + num_str[:i])
        if not is_prime(new_number):
            return False
    return True

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True





 # Examples
print(is_circular_prime(197) == True)
print(is_circular_prime(19) == False)  # 19 is prime but 91 is not
print(is_circular_prime(991) == True)
print(is_circular_prime(13) == True)   # 13 and 31 are both prime
print(is_circular_prime(11) == True)   # Only one rotation: 11
