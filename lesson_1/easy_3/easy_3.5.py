# Reverse Number 

'''
Write a function that takes a positive integer as an argument 
and returns that number with its digits reversed.
'''

def reverse_number(number):
    str_number = str(number)[::-1]
    return int(str_number)


print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True