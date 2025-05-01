# Convert a Number to a String

'''
Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on)
to the string representation of that integer.

You may not use any of the standard conversion functions available in Python, such as str.
Your function should do this the old-fashioned way and construct the string by analyzing 
and manipulating the number.

'''

NUMBERS_TO_STRING = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number): 
    number_string = ''
    while number > 0: 
        number, digit = divmod(number, 10)
        number_string = NUMBERS_TO_STRING[digit] + number_string
    return number_string or '0'


print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True