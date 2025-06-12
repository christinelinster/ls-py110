# Practice Problem 14

'''
Create a function that takes a single integer argument and 
returns the sum of all the multiples of 7 or 11 that are less than the argument. 
If a number is a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. 
The sum of these multiples is 75.

If the argument is negative, return 0.
'''

'''
I: number
O: sum of multiples of 7 and 11 that are less than input number 

rules: 
- if negative, return 0 
- if number is multiple of 7 and 11, then count it once

ds: 
- list to store all the multiples 
- multiples, 1, 2, 3, ... (range) 
- conditionals:
    - multiple < input number 
    
- get the multiple of 7, get the multiple of 11, check if they're the same, if not then add to list 

a: 
- multiple_list
- i = 1
- while 7*i < num:
    - append (7 * i) to multiple list 
    - if 11 * i < num and 11* i != 7 * i:
- return sum of the multiple list 

'''

def seven_eleven(num):
    multiples = set() 

    max_7 = (num - 1) // 7 
    max_11 = (num - 1) // 11

    for i in range(1, max_7 + 1):
        multiples.add(7 * i)
    
    for j in range(1, max_11 + 1):
        multiples.add(11 * j)
    
    return sum(multiples)



print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)