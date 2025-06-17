# Count the letters in a string

'''Write a function that takes a string as input and counts the occurrences of each
lowercase letter in the string. Return the counts in a dictionary where the
letters are keys and their counts are values.'''

def letter_count(str):
    char_set = set(str)
    return {char: str.count(char) for char in char_set}

letter_count('launchschool') #=> { ’a’: 1, ‘c’: 2, ‘h’: 2, ‘l’: 2, ‘o’: 2, ‘u’: 1 }
print(letter_count('launchschool'))