# Practice Problem 13 
'''
Create a function that takes two strings as arguments and 
returns True if some portion of the characters in the first string 
can be rearranged to match the characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will be empty.

'''

def unscramble(str1, str2):
    if len(str1) < len(str2):
        return False
    letter_dict = {}

    for letter in str1:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1
    
    for letter in str2:
        if letter not in letter_dict or letter_dict.get(letter) == 0: 
            return False
        letter_dict[letter] = letter_dict.get(letter) - 1
    return True
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)

