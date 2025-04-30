# - set numbers = [] 
# - for each number in the 1s, 10s, 100s, etc position
# - find the associated integer value and add to the list 
# - add the numbers together in the list 

def string_to_integer(s):
    value = 0
    for char in s:
        value = (10 * value) + get_number(char)
  
    return value

def get_number(string_number):

    match string_number:
        case '1':
            return 1
        case '2': 
            return 2
        case '3':
            return 3
        case '4':
            return 4
        case '5':
            return 5
        case '6':
            return 6
        case '7':
            return 7
        case '8':
            return 8
        case '9':
            return 9
        case _:
            return 0

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True