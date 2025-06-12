# Practice Problem 15
'''
Create a function that takes a string argument that consists 
entirely of numeric digits and computes the greatest product 
of four consecutive digits in the string. 

The argument will always have more than 4 digits.
'''

def greatest_product(num_str):
    l = 0
    r = 4
    curr_max = 1
    for num in num_str[:4]:
        curr_max *= int(num) 
    
    while r < len(num_str):
        temp = curr_max // int(num_str[l]) * int(num_str[r])
        curr_max = max(curr_max, temp)
        r += 1
        l += 1
    return curr_max




print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6