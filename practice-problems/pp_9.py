# Practice Problem 9

'''
Create a function that takes two string arguments and 
returns the number of times that the second string occurs in the first string. 
Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.
'''

def count_substrings(str_1, str_2):
    count = 0 
    i = 0
    while i < len(str_1):
        starting_i = str_1.find(str_2, i)
        if starting_i == -1:
            break
        
        count += 1
        i += starting_i + len(str_2)

    return count


print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)