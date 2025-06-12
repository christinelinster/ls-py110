# Practice Problem 20

'''
Create a function that takes a list of numbers, all of which are the same except one. 
Find and return the number in the list that differs from all the rest.

The list will always contain at least 3 numbers, and there will always be exactly one number that is different.
'''

def what_is_different(num_lst):
    num_set = set(num_lst)

    for num in num_set:
        if num_lst.count(num) == 1:
            return num

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)