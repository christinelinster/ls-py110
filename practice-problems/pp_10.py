# Practice Problem 10
'''
Create a function that takes a string of digits as an argument and 
returns the number of even-numbered substrings that can be formed. 
For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', 
for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.
'''

def even_substrings(num_str):
    count = 0
    for idx, num in enumerate(num_str):
        if int(num) % 2 == 0:
            for i in range(idx + 1):
                count += 1 
    return count
    


print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)