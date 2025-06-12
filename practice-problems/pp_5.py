# Practice Problem 5 -- needs practice 

'''
Create a function that takes a string argument and 
returns the character that occurs most often in the string. 

If there are multiple characters with the same greatest frequency, 
return the one that appears first in the string. 

When counting characters, consider uppercase and lowercase versions to be the same.
'''

# I: string
# O: letter 
# Rules:
## - lower, upper are the same 
## - only letters 
## - if same frequency, return the one that appeared the most first 
## - assume spaces do not count
# DS: 
## - dictionary to store letter and frequency 
## - index of that char, returning the one with the smaller number 
# A: 
## - iterate through each letter
## - store letters and frequency in dict 
## - get the item with the highest value 
## - find index of item if there are multiple with the same value, 
## - return the char with the lower index 

def most_common_char(str):
    freq_dict = {}

    for letter in str:
        if letter.isalpha():
            freq_dict[letter.lower()] = freq_dict.get(letter.lower(), 0) + 1
    
    max_count = max(freq_dict.values())
    for char in str.lower():
        if char.isalpha() and freq_dict[char] == max_count:
            return char
    # OR 
    # return max(freq_dict, key=freq_dict.get)

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')