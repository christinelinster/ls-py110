# Convert a String to a Signed Number

def string_to_signed_integer(s):
    match s[0]:
        case '-':
            return -string_to_integer(s[1:])
        case '+':
            return string_to_integer(s[1:])
        case _:
            return string_to_integer(s)

def string_to_integer(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    value = 0
    for char in s:
        value = (10 * value) + DIGITS[char]
  
    return value

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True