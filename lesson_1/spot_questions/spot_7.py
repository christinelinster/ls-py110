# The Nth Char

'''Write a function that takes a list of words and constructs a new word by
concatenating the nth letter from each word, where n is the position of the
word in the list.'''

def nth_char(lst):
    word = ''
    for i in range(len(lst)):
        word += lst[i][i]
    return word

print(nth_char(['yoda', 'best', 'has']))
# Example:
# nth_char(['yoda', 'best', 'has']) # should return 'yes'
