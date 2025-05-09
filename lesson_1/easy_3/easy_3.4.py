# Double Char (Part 2)

'''
Write a function that takes a string, doubles every consonant
in the string, and returns the result as a new string. The function 
should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.
'''

NOT_DOUBLED = ('a', 'e', 'i', 'o', 'u')

def double_consonants(message):
    doubled = ""
    for char in message:
        if char.isalpha() and char.lower() not in NOT_DOUBLED:
            doubled += char * 2
        else:
            doubled += char

    return doubled

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")