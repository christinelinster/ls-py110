# Convert a Signed Number to a String

NUMBERS_TO_STRING = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def signed_integer_to_string(number):
    if number < 0:
        return f'-{integer_to_string(abs(number))}'
    elif number > 0: 
        return f'+{integer_to_string(abs(number))}'
    else:
        return '0'

def integer_to_string(number): 
    number_string = ''

    while number > 0: 
        number, digit = divmod(number, 10)
        number_string = NUMBERS_TO_STRING[digit] + number_string
    return number_string or '0'


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True