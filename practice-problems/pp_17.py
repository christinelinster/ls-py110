# Practice Problem 17
'''
Create a function that takes a list of integers as an argument. 
The function should determine the minimum integer value that can be 
appended to the list so the sum of all the elements equals the closest 
prime number that is greater than the current sum of the numbers. For example, 
the numbers in [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. 
Thus, we can add 1 to the list to sum to 7.

Notes:

The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.
'''



def nearest_prime_sum(num_lst):
    curr_sum = sum(num_lst)
    i = 1

    while True:
        if is_prime(curr_sum + i):
            return i
        i += 1
        

def is_prime(num):
    for i in range(2, num):
        if num != i and num % i == 0:
            return False 
    return True

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)