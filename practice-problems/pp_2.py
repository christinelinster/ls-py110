# Problem 2

'''
Create a function that takes a list of integers as an argument. 
The function should return the minimum sum of 5 consecutive numbers in the list. 
If the list contains fewer than 5 elements, the function should return None.
'''

# return num, min sum of 5 consecutive numbers in the list 
# return None if len(lst) <5 

def minimum_sum(lst):
    if len(lst) < 5:
        return None
    
    total_sum = 10000000
    l = 0 
    r = 5

    while r <= len(lst):
        total_sum = min(total_sum, sum(lst[l:r]))
        l += 1
        r += 1

    return total_sum



print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)