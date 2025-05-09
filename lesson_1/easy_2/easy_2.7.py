# Multiple Lists

'''
Write a function that takes two list arguments, 
each containing a list of numbers, and returns 
a new list that contains the product of each pair of 
numbers from the arguments that have the same index. 
You may assume that the arguments contain the same number of elements.

'''

def multiply_list(num_list_1, num_list_2):
    return [num1 * num2 for num1, num2 in zip(num_list_1, num_list_2)]



list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True