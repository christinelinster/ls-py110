# Practice Problem 4

'''
Create a function that takes a list of integers as an argument and 
returns a tuple of two numbers that are closest together in value. 

If there are multiple pairs that are equally close, 
return the pair that occurs first in the list.
'''

# sort numbers
# keep track of pairs
# get diff between each one, if difference is smaller, then update pair 
# output is tuple

def closest_numbers(lst):
    diff = float('inf')
    result = ()

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            curr_diff = abs(lst[i] - lst[j])
            if curr_diff < diff:
                diff = curr_diff
                result = (lst[i], lst[j])
    return result



  

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))