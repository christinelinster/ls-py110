# Combining Lists

'''
Write a function that takes two lists as arguments and returns a 
set that contains the union of the values from the two lists. 
You may assume that both arguments will always be lists.

'''

def union(list_1, list_2):
    return set(list_1).union(set(list_2))


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True